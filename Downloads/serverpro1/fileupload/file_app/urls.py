from django.conf.urls import url
from .views import FileUploadView

urlpatterns = [
    url('employee', FileUploadView.as_view()),
    # url('employee/<?id>', FileUploadView.as_view()),
    #url('employee/<int:id>', FileUploadView.as_view()),
]