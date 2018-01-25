from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^help/', views.help_page, name='help_page'),
    url(r'^user/', views.user_page, name='user_page'),
]
