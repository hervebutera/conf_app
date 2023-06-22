from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/update/', views.update_speaker)
]
