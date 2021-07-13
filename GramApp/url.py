from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'index'),
    url('^search/',views.search_results, name='search_results'),
    url('^post/',views.views.views.new_post, name='post'),
    url('^profile/',views.profile, name='profile'),
    url('^newpost/',views.newPost, name='newPost'),
    url('^edit_profile/',views.editProfile, name='update_Profile'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
