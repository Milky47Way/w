"""
URL configuration for task_traking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("",TaskListView.as_view(), name="task-list"),

					path("<int:pk>/",TaskDetailView.as_view(), name="task-detail"),

					path("<int:pk>/update/", TaskUpdateView.as_view(),name="task-update"),

path("<int:pk>/delete/",TaskDeleteView.as_view(), name="task-delete"),

path("task-create/",TaskCreateView.as_view(), name="task-create"),

path("<int:pk>/complete/",TaskCompleteView.as_view(), name="task-complete"),

path("comment/edit/<int:pk>/",CommentUpdateView.as_view(), name="edit_comment"),

path("comment/delete/<int:pk>/",CommentDeleteView.as_view(), name="delete_comment"),

path("comment/like/<int:pk>/",CommentLikeToggle.as_view(),

name="comment-like-toggle"),

path("login/",CustomLoginView.as_view(),name="login"),

path("logout/",CustomLogoutView.as_view(),name="logout"),

path("register/",RegisterView.as_view(),name="register"),
]
