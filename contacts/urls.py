from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.PersonListView.as_view(), name='list'),
    path('create/', views.PersonCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PersonDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.PersonUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.PersontDeleteView.as_view(), name='delete'),
]