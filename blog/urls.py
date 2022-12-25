from django.urls import path ,include
from .views import *

urlpatterns = [
    path('',dashboard, name='dashboard'),
    path('artikel',artikel, name='barang_list'),
    path('users/',users, name='tabel_users'),
    path('artikel/tambah',tambah_artikel, name='tambah_artikel'),
    path('artikel/sinkron',sinkron_artikel, name='sinkron_artikel'),
    path('artikel/lihat/<str:id>',lihat_artikel, name='lihat_artikel'),
    path('artikel/edit/<str:id>',edit_artikel, name='edit_artikel'),
    path('artikel/delete/<str:id>',delete_artikel, name='delete_artikel'),
]