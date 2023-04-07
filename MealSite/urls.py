from django.urls import path
from . import views

app_name = 'meal'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('meal/tag/<str:tag>/', views.TagView.as_view(), name='tag'),
    path('meal/detail/<int:pk>/', views.MealDetailView.as_view(), name='detail'),
    path('meal/create/', views.MealCreateView.as_view(), name='create'),
    path('meal/<int:pk>/delete/', views.MealDeleteView.as_view(), name='delete'),
    path('meal/<int:pk>/update/', views.MealUpdateView.as_view(), name='update'),
]