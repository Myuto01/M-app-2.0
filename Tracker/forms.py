from django import forms
from .models import Habit, NotepadEntry, Goal, Resource, BookRecommendation, MeditationExercise, Image

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name']

class NotepadForm(forms.ModelForm):
    class Meta:
        model = NotepadEntry
        fields = ['journal_entry', 'voice_note', 'images']
        widgets = {
            'journal_entry': forms.Textarea(attrs={'class': 'journal_entry' }),
        }

class NotepadEditForm(forms.ModelForm):
    class Meta:
        model = NotepadEntry
        fields = ['journal_entry', 'voice_note', 'images']

class GoalForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'title-form'}))
    class Meta:
        model = Goal
        fields = ['title', 'description', 'target_date']
        widgets = {
        'target_date': forms.DateInput(attrs={'type': 'date', 'id': 'id_target_date'}),
        'description': forms.Textarea(attrs={'class': 'description-form' }),
        }

class GoalEditForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'title-input'}))
    class Meta:
        model = Goal
        fields = ['title', 'description', 'target_date']
        widgets = {
        'target_date': forms.DateInput(attrs={'type': 'date'}),
        'description': forms.Textarea(attrs={'class': 'description-input' }),
        }

class ResourceForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'title-input'}))
    url = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 400px;'}))
    category = forms.CharField(widget=forms.TextInput(attrs={'class': 'category-input'}))
    class Meta:
        model = Resource
        fields = ['title', 'description', 'url', 'category']
        widgets = {
        'description': forms.Textarea(attrs={'class': 'description-input' }),
        }
    

class BookRecommendationForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'title-input'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'class': 'title-input'}))
    amazon_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'title-input'}))
    category = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 200px;'}))
    class Meta:
        model = BookRecommendation
        fields = ['title', 'author', 'description', 'amazon_url', 'category']
        widgets = {
        'description': forms.Textarea(attrs={'class': 'description-input' }),
        }

class MeditationExerciseForm(forms.ModelForm):
    class Meta:
        model = MeditationExercise
        fields = ['title', 'description', 'content', 'category']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image 
        fields = ['image']

