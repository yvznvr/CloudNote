"""notebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from note import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api', views.NoteViewSet, base_name='NoteViewSet')


urlpatterns = [
    url(r'^$', views.MainPage.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.UserLogin.as_view(), name='login'),
    url(r'^usercreate/$', views.UserCreate.as_view(), name='user-create'),
    url(r'^logout/$', views.UserLogout.as_view(), name='logout'),
    url(r'^notlar/$', views.NoteList.as_view(), name='note_list'),
    url(r'^notlar/create/$', views.NoteCreate.as_view(), name='note-create'),
    url(r'^notlar/update/(?P<pk>[-\w]+)/$', views.NoteUpdate.as_view(), name='note-update'),
    url(r'^notlar/delete/(?P<pk>[-\w]+)/$', views.NoteDelete.as_view(), name='note-delete'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]