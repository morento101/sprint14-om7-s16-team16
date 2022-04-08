from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.authors_list, name='authors_list'),
    url(r'create/', views.author_create, name='author_create'),
    path('delete/<int:a_id>/', views.author_delete, name='author_delete'),
    path('update/<int:a_id>/', views.author_update, name='author_update')
]