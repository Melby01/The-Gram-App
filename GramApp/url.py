from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^login/',views.login, name = 'login'),
    url('^register/',views.register, name= 'register'),
    url('^search/',views.search_results, name='search_results')
]