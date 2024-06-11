from django.contrib import admin
from .models import Habit, NotepadEntry, Goal, Resource, BookRecommendation, MeditationExercise, Image, BlockedWebsite


admin.site.register(Habit)

admin.site.register(NotepadEntry)

admin.site.register(Goal)

admin.site.register(Resource)

admin.site.register(MeditationExercise)

admin.site.register(BookRecommendation)

admin.site.register(Image)

admin.site.register(BlockedWebsite)


