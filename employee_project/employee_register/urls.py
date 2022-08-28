from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.employee_form, name='employee_insert'), # get and post req.for insert
    path('<int:id>/',views.employee_form,name='employee_update' ),#get post fot update
    path('list/',views.employee_list,name='employee_list')# display recd
]
