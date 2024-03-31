from django.db import models
from django.contrib.auth.models import User
from django.db.models import ImageField
from django.utils import timezone
from datetime import datetime, timedelta


class Habit(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField( default=None)
    month_added = models.CharField(max_length=20, default = timezone.now)  # Field to store the month

    def save(self, *args, **kwargs):
        # Set the month_added field before saving
        self.month_added = datetime.now().strftime('%B')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Habit

    def delete_habit(self):
        # Implement any additional logic you need before deleting the habit
        self.delete()

# NotePad
class NotepadEntry(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    journal_entry = models.TextField()
    voice_note = models.FileField(upload_to='voice_notes/', null=True, blank=True)
    images = models.FileField(upload_to='images/', null=True, blank=True)

# Goal Setting 
class Goal(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    target_date = models.DateField()
    is_achieved = models.BooleanField(default=False)

    def mark_achieved(self):
        self.is_achieved = True
        self.save()

class Resource(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    category = models.CharField(max_length=50)  # You can use choices for predefined categories

    def __str__(self):
        return self.title

# models.py
class BookRecommendation(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    amazon_url = models.URLField()
    category = models.CharField(max_length=255, default=None)


    def __str__(self):
        return self.title


class MeditationExercise(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()  # You can use this field for exercise script or audio link
    category = models.CharField(max_length=50)  # You can use choices for predefined categories

    def __str__(self):
        return self.title

class Image(models.Model):
    image = ImageField(null=False, blank=False, upload_to='images/', default="")


   
# Time Table
class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)

    
