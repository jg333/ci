from django.urls import path

from . import views

app_name = "message_app"

urlpatterns = [
    path('messages', views.MessageList.as_view(), name='message_list'),
    path('message/<int:pk>', views.MessageDetail.as_view(), name='message_detail'),
    path('create', views.MessageCreate.as_view(), name='message_create'),
    path('update/<int:pk>', views.MessageUpdate.as_view(), name='message_update'),
    path('delete/<int:pk>', views.MessageDelete.as_view(), name='message_delete'),
]