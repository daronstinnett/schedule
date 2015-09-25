from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row
from django import forms

from schedule.bookings.models import Booking
from schedule.projects.models import Project
from schedule.resources.models import Resource


class BookingForm(forms.ModelForm):
    id = forms.Field(required=False, widget=forms.HiddenInput())
    project = forms.ModelChoiceField(Project.objects.all(), required=False, widget=forms.HiddenInput())
    resource = forms.ModelChoiceField(Resource.objects.all())
    start = forms.DateTimeField()
    end = forms.DateTimeField()

    class Meta:
        model = Booking
        fields = ['id','resource', "start", "end", 'project']
    
    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-8'
        self.helper.layout = Layout(
            Field('id'),
            Field('project', css_class="project_input"),
            Field('resource', css_class="select2", style="visibility:hidden;width:100%;"),
            Row('start_date', 'start_time'),
        )
                