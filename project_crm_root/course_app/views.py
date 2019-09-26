from django.shortcuts import render, HttpResponseRedirect
from .course_form import CourseForm
from .models import CouseModel
from django.urls import reverse


# Create your views here.

def index(request):
    # create isntance of form class
    form1 = CourseForm()
    courses = CouseModel.objects.all()

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

    # pass both the form object and courses query in a dictionary, then only both shown in same page
    return render(request, 'course_app/index.html', {'myform': form1, 'objs': courses})


def delete(request, course_id):
    course = CouseModel.objects.filter(id=course_id)
    course.delete()
    return index(request)


def edit(request, new_id):
    cours = CouseModel.objects.filter(id=new_id).first()
    # Create a form to edit an existing data, but use
    # POST data to populate the form.
    form2 = CourseForm(request.POST, instance=cours)
    if form2.is_valid():
        form2.save(commit=True)
        # to redirect to the index page after saving to db
        return HttpResponseRedirect(reverse('myapp:index'))
    return render(request, 'course_app/edit.html', {'newform': form2})
