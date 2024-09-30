from django.urls import path
from .views import ContactCreateView, ProjectListCreateView, ProjectDetailView, AchievementListCreateView, AchievementDetailView

urlpatterns = [
    path('contacts/', ContactCreateView.as_view(), name='contact-create'),
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('achievements/', AchievementListCreateView.as_view(), name='achievement-list-create'),
    path('achievements/<int:pk>/', AchievementDetailView.as_view(), name='achievement-detail'),
]