from django.contrib import admin
from django.urls import path, include
from contact.views import (
    ContactCreateView, ProjectListCreateView, ProjectDetailView,
    AchievementListCreateView, AchievementDetailView,
    ClientReviewListCreateView, ClientReviewDetailView
)
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/contacts/', ContactCreateView.as_view(), name='contact-create'),
    path('api/projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('api/projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('api/achievements/', AchievementListCreateView.as_view(), name='achievement-list-create'),
    path('api/achievements/<int:pk>/', AchievementDetailView.as_view(), name='achievement-detail'),
    path('api/reviews/', ClientReviewListCreateView.as_view(), name='review-list-create'),
    path('api/reviews/<int:pk>/', ClientReviewDetailView.as_view(), name='review-detail'),
]