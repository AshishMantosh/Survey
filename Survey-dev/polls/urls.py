from django.urls import path
from .views import listPolls, vote


app_name = "polls"
urlpatterns = [
    path('<str:username>/', listPolls, name="polls"),
    path('<str:username>/<int:question_id>/', vote, name="vote"),
]
