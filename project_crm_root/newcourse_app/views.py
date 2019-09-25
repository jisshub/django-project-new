from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'newcourse_app/index.html')


def course_add(request):
    return render(request, 'newcourse_app/add_course.html')


def list_course(request):
    return render(request, 'newcourse_app/list_course.html')
