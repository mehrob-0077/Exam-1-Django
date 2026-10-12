from django.urls import path
from .views import *

urlpatterns = [
    path("",kino_list_view,name="kino_list"),
    path("create/",kino_create_view,name="kino_create"),
    path("update/",kino_update_view,name="kino_update"),
    path("dalete/",kino_dalete_view,name="kino_dalete"),
]