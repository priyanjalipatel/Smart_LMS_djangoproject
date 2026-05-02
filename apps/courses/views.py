from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from .models import Course
from .forms import RegisterForm

def home(request):
    courses = Course.objects.all()[:3]
    return render(request, 'courses/home.html', {'courses': courses})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'courses/register.html', {'form': form})
