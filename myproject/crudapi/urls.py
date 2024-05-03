from django.urls import path
from . import views 
urlpatterns=[


    path('get/<str:name>',views.get_data,name='get'),
    path('post/<str:name>/<int:roll_no>',views.post_data,name='post'),
    path('put/<str:name>/<str:new_name>',views.put_data,name='put'),
    path('delete/<int:roll_no>',views.delete_data,name='delete')
]