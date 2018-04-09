from django.conf.urls import include, url
from cart import views
urlpatterns = [
    url(r'^cart_count/$',views.cart_count,name='cart_count'),
    url(r'^cart_add/$',views.cart_add,name='cart_add'),
    url(r'^$',views.cart_show,name='cart'),
    url(r'^del/$', views.cart_del, name='delete'), # 购物车商品记录删除
]
