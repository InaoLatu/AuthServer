from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from students_manager.forms import StudentCreateForm, UserCreateForm
from students_manager.models import Student


def signup(request):
    if request.method == 'POST':
        user_form = UserCreateForm(request.POST)
        student_form = StudentCreateForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            student = Student.objects.create(user=user, faculty="teleco")
            student.save()

            return render(request, 'students_manager/confirm_registration.html')
    else:
        user_form = UserCreateForm()
        student_form = StudentCreateForm()

    return render(request, 'students_manager/signup.html', {'user_form': user_form, 'student_form': student_form})


# Register the third-platform id of choice. It could be the id from telegram, alexa or moodle
def register_id(request, **kwargs):
    try:
        user = User.objects.get(username=kwargs['username'])
        student = Student.objects.get(user=user)

        if kwargs['type'] == 'telegram':
            student.telegram_id = kwargs['id']
        elif kwargs['type'] == 'alexa':
            student.alexa_id = kwargs['id']
        elif kwargs['type'] == 'moodle':
            student.moodle_id = kwargs['id']
        else:
            return HttpResponse("Type not correct. Options available are: 'telegram', 'alexa' and 'moodle'", status=400)

        student.save()

    except User.DoesNotExist:
        return HttpResponse("User does not exist", status=404)

    return HttpResponse("Id registered", status=200)
