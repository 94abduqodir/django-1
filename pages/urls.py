from django.urls import path
from .views import HomePageViews, AboutPageViews

urlpatterns = [
    path('', HomePageViews.as_view(), name='home'),
    path('about/', AboutPageViews.as_view(), name='about')
]
