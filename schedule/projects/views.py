from django.core.urlresolvers import reverse_lazy
from django.forms.models import modelformset_factory
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.list import ListView
from rest_framework import viewsets, renderers

from schedule.bookings.forms import BookingForm
from schedule.bookings.models import Booking
from schedule.common.renderers import SelectJSONRenderer
from schedule.projects.models import Project
from schedule.projects.serializers import ProjectSerializer


# API
class ProjectAPIViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    renderer_classes = (
        renderers.JSONRenderer, 
        renderers.BrowsableAPIRenderer, 
        SelectJSONRenderer)
    
# Standard Views
class BaseProjectView(object):
    model = Project
    queryset = Project.objects.all()
    
class ProjectListView(BaseProjectView, ListView):
    pass

class ProjectCreateUpdateBase(BaseProjectView):
    success_url = reverse_lazy('projects:list')
    fields = [
        'name',
        'type',
        'contract',
        'notes'
    ]
    
    def __init__(self):
        self.BookingFormSet = modelformset_factory(
            Booking, form=BookingForm, extra=1)
    
    def dispatch(self, request, *args, **kwargs):
        self.project = self.get_object() if self.kwargs.get('pk') else None
        self.success_url = self.request.GET.get('success_url', self.success_url)
        return super(ProjectCreateUpdateBase, self).dispatch(request, *args, **kwargs)
    
    def form_invalid(self, form, formset):
        """
        override to render both the form and formset to context
        """
        return self.render_to_response(self.get_context_data(form=form, formset=formset))    
    
    def form_valid(self, form, formset):
        """
        override to save both the form and formset
        """
        bookings = formset.save(commit=False)
        response = super(ProjectCreateUpdateBase, self).form_valid(form)
        for booking in bookings:
            if not booking.project_id:
                booking.project_id = form.instance.id
            booking.save()
        return response

    def get_context_data(self, **kwargs):
        data = super(ProjectCreateUpdateBase, self).get_context_data(**kwargs)
        if self.request.method == "GET":
            if self.project:
                queryset = self.project.bookings.order_by("start")
            else:
                queryset = Booking.objects.none()
            formset = self.BookingFormSet(
                queryset=queryset,
            )
            data.update({'formset': formset})
            data.update({'extra_form': formset[-1:]})
        data.update({'success_url': self.success_url})
        return data
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        formset = self.BookingFormSet(request.POST)
        form = self.get_form()
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)


class ProjectUpdateView(ProjectCreateUpdateBase, UpdateView):
    
    def dispatch(self, request, *args, **kwargs):
        self.booking_pk = int(self.request.GET.get('booking', 0))
        return super(ProjectUpdateView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        data = super(ProjectUpdateView, self).get_context_data(**kwargs)
        serializer = ProjectSerializer(self.object, context={'request': self.request})
        project_as_json = renderers.JSONRenderer().render(serializer.data)
        data.update({
            'project': data['object'],
            'booking_pk': self.booking_pk,
            'project_as_json': project_as_json
        })
        return data

class ProjectCreateView(ProjectCreateUpdateBase, CreateView):
    pass
