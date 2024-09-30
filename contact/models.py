from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name if self.name else 'Unnamed Contact'
    

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tools = models.JSONField(blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    demo = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name if self.name else 'Unnamed Project'

class Achievement(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    

    def __str__(self):
        return self.title if self.title else 'Unnamed Achievement'


REVIEW_CHOICES = (
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
)
    
class ClientReview(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    desciption = models.TextField(blank=True, null=True)
    review = models.CharField(max_length=10, choices=REVIEW_CHOICES, blank=True, null=True)


    def __str__(self):
        return self.name if self.name else 'Unnamed Review'