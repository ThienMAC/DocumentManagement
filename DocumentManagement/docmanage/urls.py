from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("subsystem_list/",views.subsystem_list,name="subsystem_list"),
    path("document_list/",views.document_list,name="document_list"),
    path("subsys_create/",views.subsys_create,name="subsys_create"),
    path("document_create/",views.document_create,name="document_create"),
    path("subsystem_detail/<int:subsys_id>/",views.subsystem_detail,name="subsystem_detail"),
    path("<int:document_id>/",views.document_detail,name="document_detail"),
    
]
