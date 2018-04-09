from django.conf.urls import include, url
from book import views
urlpatterns = [
    url(r'^$', views.index, name='index'),  # 首页
    url(r'^detail/(?P<id>.*)$',views.detail,name='detail'),
    url(r'^list/(?P<type_id>.+)/(?P<page>.+)$',views.list,name='list'),
]
