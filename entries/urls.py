from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = staticfiles_urlpatterns()


urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add, name='add'),
    path('add2/', views.add, name='add2')
]
