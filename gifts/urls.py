from django.urls import path
from . import views

app_name = 'gifts'

urlpatterns = [
    path('', views.GiftListView.as_view(), name='list'),
    path('create/', views.GiftCreateView.as_view(), name='create'),
    path('<int:pk>/', views.GiftDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.GiftUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.GiftDeleteView.as_view(), name='delete'),
]