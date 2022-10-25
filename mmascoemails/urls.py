from django.urls import path
from mmascoemails.views import emails_view,EmailCreateView

urlpatterns =[
    path("", EmailCreateView.as_view(), name="email_view")
]