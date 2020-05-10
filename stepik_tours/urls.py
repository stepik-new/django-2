from django.contrib import admin
from django.urls import path

from tours.views import DepartureView, TourView, MainView

urlpatterns = [
    path('', MainView.as_view()),
    path('departure/<str:departure>/', DepartureView.as_view()),
    path('tour/<int:id>/', TourView.as_view()),
    path('admin/', admin.site.urls),
]
