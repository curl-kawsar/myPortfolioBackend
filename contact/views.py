from rest_framework import generics
from .models import Contact, Project, Achievement, ClientReview
from .serializers import ContactSerializer, ProjectSerializer, AchievementSerializer, ClientReviewSerializer

class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class AchievementListCreateView(generics.ListCreateAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class AchievementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class ClientReviewListCreateView(generics.ListCreateAPIView):
    queryset = ClientReview.objects.all()
    serializer_class = ClientReviewSerializer

class ClientReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClientReview.objects.all()
    serializer_class = ClientReviewSerializer