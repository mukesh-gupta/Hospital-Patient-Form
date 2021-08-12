from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
   path('list',views.patient_list,name='list'),
   path('create/',views.create,name='create'),
  path('detail/<int:pk>',views.detail,name='detail'),
 path('update/<int:pk>',views.update,name='update'),
 path('delete/<int:pk>',views.delete,name='delete'),
#    path('up/<int:pk>',views.person_update,name='up')
]

