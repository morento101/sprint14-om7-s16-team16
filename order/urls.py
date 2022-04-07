from django.urls import path
from . import views


urlpatterns = [
    path('order_list/', views.OrderList.as_view(), name='order_list'),
    path('order_whitelist/', views.FilteredOrderList.as_view(), name='order_whitelist'),

    path('create_order/', views.OrderFormView.as_view(), name='create_order'),
    path('update_order/<int:order_id>/', views.OrderFormView.as_view(), name='update_order'),
    path('delete_order/<int:order_id>/', views.DeleteOrderView.as_view(), name='delete_order'),
]