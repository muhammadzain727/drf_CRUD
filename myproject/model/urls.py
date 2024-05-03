from django.urls import path
from . import views 

urlpatterns=[
    
    path('post/<str:state>/<str:city>/<int:postal_code>',views.create,name="create"),
    path('get/<int:postal_code>',views.read,name="read"),
    path('put/<int:id>/<str:state>/<str:city>/<int:postal_code>',views.update,name="update"),
    path('delete/<int:postal_code>',views.delete,name="delete"),
    path('exclude/',views.filtered_countries_view,name="exclude"),
    path('annotate/',views.entries_no,name="annotate"),
    path('get_method/<int:id>',views.get_method,name="read"),
    path('orderby/',views.orderby_,name="annotate"),
]