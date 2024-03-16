from turnos import views
from api.views import LoginUserAPIView, RegisterUserAPIView
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("turnos", views.TurnosAPIListView.as_view()),
    path('turnos/<int:pk>', views.TurnosDetailView.as_view()),
    path('auth/login', LoginUserAPIView.as_view()),
    path('auth/register', RegisterUserAPIView.as_view()),
    # path("auth/", include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)