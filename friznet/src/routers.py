from django.urls import path, include

urlpatterns = [
    path('<int:pk>/', include('src.profiles.urls')),
]