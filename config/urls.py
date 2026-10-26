from django.contrib import admin
from django.urls import path, include
from celebrations.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('celebrations/', include('celebrations.urls')),
    path('contacts/', include('contacts.urls')),
    path('gifts/', include('gifts.urls')),

]