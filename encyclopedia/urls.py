from django.urls import path

from . import views
app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("create_new/", views.create_new, name="create_new"),
    path("wiki/<str:title>", views.search, name="title"),
    path("clicked_entry/<str:entry>", views.clicked_entry, name="clicked_entry"),
    path("random/", views.random_func, name="random"),
    path("edit/<str:t>/", views.edit, name="edit"),
    path("searching_entry/",views.search_entries,name="search_entries")
]
