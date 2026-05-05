from django.urls import path
from .views import confessions,react_confession,add_comment,get_comments,delete_comment

urlpatterns = [
  path('confessions/', confessions),
  path('confessions/<uuid:confession_id>/react/', react_confession),
  path('confessions/<uuid:confession_id>/comment/', add_comment),
  path('confessions/<uuid:confession_id>/comments/', get_comments),
  path('comments/<int:comment_id>/delete/', delete_comment),
]