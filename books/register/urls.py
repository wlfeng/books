from django.conf.urls import include, url
from register import views
urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^login_handler/$',views.register_handler,name='register_handler'),
    url(r'^login/$',views.login,name='login'),
    url(r'^$', views.user,name = 'user'),
    url(r'^login_check/$',views.login_check,name='login_check'),
]
