from django.urls import path,include
from blog import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='blog/index.html')),
]
