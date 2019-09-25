from django.shortcuts import render
from .course_form import CourseForm
from .models import CouseModel


# Create your views here.

def index(request):
    # create isntance of form class
    form1 = CourseForm()
    # check whether request method is post
    if request.method == 'POST':
        # if, ok later create an instance of that submitted form. ie form posted to server
        form = CourseForm(request.POST)
        # validate data submitted in form
        if form.is_valid():
            # later save that form object to db.
            form.save(commit=True)
            # if all ok then return that template rendered in index view.
            return index(request)
    else:
        print('Error')
    return render(request, 'course_app/index.html', {'myform': form1})


def course_list(request):
    courses_list = CouseModel.objects.all()
    # pass the query set to a dictionary as value
    context = {
        'courses': courses_list
    }
    return render(request, 'course_app/courses.html', context)


def delete_course(request, course_id):
    CouseModel.objects.filter(id=course_id).delete()
    return course_list(request)


def edit_course(request, course2_id):
    specific = CouseModel.objects.filter(id=course2_id)
    context = {
        'c-spec': specific
    }
    return render(request, 'course_app/edit.html', context)
