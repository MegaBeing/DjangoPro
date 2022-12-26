from django.urls import path
from . import views
urlpatterns = [
    path("",views.mainPage,name="mainPage"),
    path("posts/",views.index,name="index"),
    path("posts/<slug>",views.posts,name='posts')
]
