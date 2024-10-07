from django.contrib import admin
from django.urls import path
from quality_checker_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('analyze_code/', views.analyze_code, name='analyze_code'),
    path('trigger_error/', views.trigger_error, name='trigger_error'),
]