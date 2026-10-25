from django.urls import path
from . import views

app_name = 'celebrations'

urlpatterns = [
    path('', views.CelebrationListView.as_view(), name='list'),
    path('create/', views.CelebrationCreateView.as_view(), name='create'),
    path('<int:pk>/', views.CelebrationDetailView.as_view(), name='detail'),
]