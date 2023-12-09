# file_upload_app/urls.py

from django.urls import path
from .views import register, file_upload, file_list, user_search, file_share, custom_login_view

urlpatterns = [
    path('register/', register, name='register'),
    path('upload/', file_upload, name='file_upload'),
    path('file_list/', file_list, name='file_list'), 
    path('user_search/', user_search, name='user_search'), 
    path('file_share/<int:file_id>/', file_share, name='file_share'), 
    path('login/', custom_login_view, name='login'),
]
