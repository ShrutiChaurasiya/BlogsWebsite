from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="Home"),
    path("delete_blog/<int:id>",views.delete_blog,name="delete_blog"),
    path("update/<int:id>",views.update,name="update"),
    path("addblog/",views.addblog,name="addblog")
]