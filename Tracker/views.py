from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseServerError, HttpResponse, JsonResponse
from django.contrib import messages
from django.conf import settings 
from .models import Habit, NotepadEntry, Goal, Resource, BookRecommendation, MeditationExercise, Image, Events
from .forms import HabitForm, NotepadForm, NotepadEditForm, GoalForm, ResourceForm, BookRecommendationForm, MeditationExerciseForm, ImageForm, GoalEditForm
from datetime import datetime
import img2pdf
from PIL import Image as PILImage
import os

def homepage(request):
    current_date = datetime.now()
    context = {'current_date': current_date}
    return render(request, 'homepage.html', context)

def add_habits(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.date_added = datetime.now()  # Set the current date and time
            habit.month_added = datetime.now().strftime('%B')  # Set the current month
            habit.save()
            return redirect('add-habits')  # Redirect to a success page
    else:
        form = HabitForm()

    selected_month = datetime.now().strftime('%B')  # Get the current month
    context = {'selected_month': selected_month, 'form': form}
    return render(request, 'add_habit.html', context)

def habit_list(request):
    habits = Habit.objects.all()
    selected_month = datetime.now().strftime('%B') 
    context =  {'selected_month': selected_month, 'habits': habits}
    return render(request, 'habit_list.html', context)

def delete_habit(request, habit_id):
    habit = get_object_or_404(Habit, pk=habit_id)

    if request.method == 'POST':
        habit.delete()
        return redirect('habit-list')
    
    context = {'habit': habit}
    return render(request, 'delete_habit.html', context)

def mark_completed(request, month, habit_id):
    habit = get_object_or_404(Habit, pk=habit_id)
    monthly_log = get_object_or_404(MonthlyLog, month=month)
    # Logic to mark habit as completed for the day (similar to the previous example)
    return habit_list(request, month)

# ===== Notes ===== 
def notepad(request):
    if request.method == 'POST':
        form = NotepadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Done')
            return redirect('notes')
        else:
            messages.error(request, 'Form is not valid. Please correct errors.')
    else:
        form = NotepadForm()

    notes = NotepadEntry.objects.all()
   
    current_date = datetime.now()
    context = {'form': form, 'current_date': current_date, 'notes': notes}
    return render(request, 'notepad.html', context)

def note_detail(request, note_id):
    note = NotepadEntry.objects.get(pk=note_id)
    context = {'note': note}
    return render(request, 'note_detail.html', context)

def notes(request):
    form = NotepadForm()
    notes = NotepadEntry.objects.all()
    context = {'notes': notes, 'form': form}
    return render(request, 'notes.html', context)

def edit_notepad(request, note_id):
    note = get_object_or_404(NotepadEntry, pk=note_id)

    if request.method == 'POST':
        form = NotepadEditForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note updated successfully.')
            return redirect('note-detail', note_id=note_id)
    else:
        form = NotepadEditForm(instance=note)

    context = {'form': form, 'note': note}
    return render(request, 'edit_notepad.html', context)

def delete_note(request, note_id):
    note = get_object_or_404(NotepadEntry, pk=note_id)
    note.delete()
    return redirect('notes')
    
    context = {' note':  note}
    return render(request, 'notes.html', context)

# ====== GOALS =====
def goal_list(request):
    goals = Goal.objects.filter()
    return render(request, 'goal_list.html', {'goals': goals})

def goal_detail(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id)

    if request.method == 'POST' and 'mark_achieved' in request.POST:
        goal.mark_achieved()
        return redirect('goal-detail', goal_id=goal_id)

    return render(request, 'goal_detail.html', {'goal': goal})

def create_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.save()
            return redirect('goal-list')
    else:
        form = GoalForm()
    return render(request, 'create_goal.html', {'form': form})

def edit_goal(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id)

    if request.method == 'POST':
        form = GoalEditForm(request.POST, request.FILES, instance=goal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Goal updated successfully.')
            return redirect('goal-detail', goal_id=goal_id)
    else:
        form = GoalEditForm(instance=goal)

    context = {'form': form, 'goal': goal}
    return render(request, 'edit_goal.html', context)

def delete_goal(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id)
    goal.delete()
    return redirect('goal-list')
    
    context = {'goal': goal}
    return render(request, 'goal_list.html', context)

# ===== Resources =====
def resources(request):
    resources_list = Resource.objects.all()
    return render(request, 'resources.html', {'resources_list': resources_list})

def add_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resources')  # Redirect to the resources page after adding a resource
    else:
        form = ResourceForm()

    return render(request, 'add_resource.html', {'form': form})

def edit_resource(request, resource_id):
    resource = Resource.objects.get(pk=resource_id)
    
    if request.method == 'POST':
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('resources')  # Redirect to the resources page after editing a resource
    else:
        form = ResourceForm(instance=resource)

    return render(request, 'edit_resource.html', {'form': form, 'resource': resource})


def delete_resource(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    resource.delete()
    return redirect('resources')
    
    context = {'resource': resource}
    return render(request, 'resource_list.html', context)

# ===== Book Recommendation ===== #
def add_book_recommendation(request):
    if request.method == 'POST':
        form = BookRecommendationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-recommendations')  # Redirect to the book recommendations page after adding a recommendation
    else:
        form = BookRecommendationForm()

    return render(request, 'add_book_recommendation.html', {'form': form})

def edit_book_recommendation(request, book_id):
    book = BookRecommendation.objects.get(pk=book_id)
    
    if request.method == 'POST':
        form = BookRecommendationForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-recommendations')  # Redirect to the book recommendations page after editing a recommendation
    else:
        form = BookRecommendationForm(instance=book)

    return render(request, 'edit_book_recommendation.html', {'form': form, 'book': book})

def book_recommendations(request):
    books_list = BookRecommendation.objects.all()
    return render(request, 'books.html', {'books_list': books_list})

def delete_book(request, book_id):
    book = get_object_or_404(BookRecommendation, pk=book_id)
    book.delete()
    return redirect('book-recommendations')
    
    context = {'book': book}
    return render(request, 'books.html', context)

# ===== Meditation Exercises ===== #
def guided_exercises(request):
    exercises_list = MeditationExercise.objects.all()
    return render(request, 'guided_exercises.html', {'exercises_list': exercises_list})


def add_meditation_exercise(request):
    if request.method == 'POST':
        form = MeditationExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guided-exercises')  # Redirect to the guided exercises page after adding an exercise
    else:
        form = MeditationExerciseForm()

    return render(request, 'add_meditation_exercise.html', {'form': form})

def edit_meditation_exercise(request, exercise_id):
    exercise = MeditationExercise.objects.get(pk=exercise_id)
    
    if request.method == 'POST':
        form = MeditationExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('guided-exercises')  # Redirect to the guided exercises page after editing an exercise
    else:
        form = MeditationExerciseForm(instance=exercise)

    return render(request, 'edit_meditation_exercise.html', {'form': form, 'exercise': exercise})

def delete_exercise(request, exercise_id):
    exercise= get_object_or_404(MeditationExercise, pk=exercise_id)
    exercise.delete()
    return redirect('guided-exercises')
    
    context = {'exercise': exercise}
    return render(request, 'guided_exercises.html', context)

def image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            image_instance = form.save()
            image_path = os.path.join(settings.MEDIA_ROOT, str(image_instance.image))

            with open(image_path, 'rb') as img:
                pdf_bytes = img2pdf.convert(img, encoding='utf8')

            # Prepare the response
            response = HttpResponse(pdf_bytes, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{image_instance.image.name}.pdf"'
            messages.success(request, 'Image converted to PDF successfully.')
            return response
        else:
            messages.error(request, 'Form is not valid. Please check the input.')

    else:
        form = ImageForm()

    context = {'form': form}
    return render(request, 'img2pdf.html', context)

    # Create your views here.
def timetable_events(request):  
    all_events = Events.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'timetable_events.html',context)
 
def all_events(request):                                                                                                 
    all_events = Events.objects.all()                                                                                    
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({                                                                                                     
            'title': event.name,                                                                                         
            'id': event.id,                                                                                              
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),                                                             
        })                                                                                                               
                                                                                                                      
    return JsonResponse(out, safe=False) 
 
def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)
 
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)
 
def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)

def countdown_timer(request):
    return render(request, 'countdown_timer.html')

"""
#Time Table
def timetable_list(request):
    events = TimetableEvent.objects.all().values()  # Convert QuerySet to a list of dictionaries
    context = {'events': list(events)}
    return render(request, 'timetable_events.html', context)

#def add_timetable_event(request):
   # if request.method == 'POST':
        #form = TimetableEventForm(request.POST)
       # if form.is_valid():
            form.save()
            return redirect('timetable-list')
    else:
        form = TimetableEventForm()
    context = {'form': form}
    return render(request, 'add_timetable_event.html', context)


#def edit_timetable_event(request, event_id):
   # event = TimetableEvent.objects.get(pk=event_id)

    #if request.method == 'POST':
     #   form = TimetableEventForm(request.POST, instance=event)
       # if form.is_valid():
        #    form.save()
           # return redirect('timetable_list')
   # else:
        #form = TimetableEventForm(instance=event)

   # context = {'form': form, 'event': event}
   #return render(request, 'templates/TimeTable/add_timetable_event.html', context)


#def delete_timetable_event(request, event_id):
    #event = get_object_or_404(TimetableEvent, pk=event_id)
    #event.delete()

    # Redirect to the timetable list view
    #return redirect('timetable-list')

#
def timetable_events(request):
   
    data = []
    for event in events:
        data.append({
            'title': event.title,
            'start': event.get_start_datetime(),  # You need to implement get_start_datetime() in your model
            'end': event.get_end_datetime(),      # You need to implement get_end_datetime() in your model
            'allDay': False,  # Set to True if the event spans the whole day
        })

    return JsonResponse(data, safe=False)

"""