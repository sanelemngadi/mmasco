from django.urls import path
from mmascoemails.views import EmailCreateView

urlpatterns =[
    path("", EmailCreateView.as_view(), name="email_view")
]