from django.conf.urls import url

from schedule.projects.views import ProjectUpdateView, ProjectListView, \
    ProjectCreateView


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ProjectUpdateView.as_view(), name="update"),
    url(r'^new/$', ProjectCreateView.as_view(), name="create"),
    url(r'$', ProjectListView.as_view(), name="list"),
]  