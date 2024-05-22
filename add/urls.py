from django.urls import path

from . import views

app_name = "add"
urlpatterns = [
	path("", views.index, name="add-page"),
	path("todos/<int:id>", views.todos, name="detail-add"),
	path("todos/post/<int:id>", views.todos, name="add-post")
]