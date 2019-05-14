from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index.html'),
    path('delete/<List_id>', views.delete, name='delete'),
    path('cross_off/<List_id>', views.cross_off, name='cross_off'),
    path('uncross/<List_id>', views.uncross, name='uncross'),
    path('editar/<List_id>', views.editar, name='editar'),

]
