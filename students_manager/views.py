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
            print(request.POST['birth_date'])
            student = Student.objects.create(user=user, faculty="teleco", birth_date=request.POST['birth_date'])
            student.save()

            return render(request, 'students_manager/confirm_registration.html')
    else:
        user_form = UserCreateForm()
        student_form = StudentCreateForm()

    return render(request, 'students_manager/signup.html', {'user_form': user_form, 'student_form': student_form})


# Register the third-platform id of choice. It could be the id from telegram, alexa or moodle
def identification_telegram(request, **kwargs):
    try:
        user = User.objects.get(username=kwargs['username'])
        student = Student.objects.get(user=user)

        if kwargs['type'] == 'telegram':
            student.telegram_id = kwargs['id']
        # elif kwargs['type'] == 'alexa':
        #     student.alexa_id = kwargs['id']
        # elif kwargs['type'] == 'moodle':
        #     student.moodle_id = kwargs['id']
        else:
            return HttpResponse("Type not correct. Options available are: 'telegram'", status=400)

        student.save()

    except User.DoesNotExist:
        return HttpResponse("User does not exist", status=404)

    return HttpResponse("Telegram id registered", status=200)

def identification_alexa(request, **kwargs):
    try:
        user = User.objects.get(first_name=kwargs['name'], last_name=kwargs['last_name'], student__birth_date=kwargs['birth_date'])
        student = Student.objects.get(user=user)
        student.alexa_id = kwargs['id']
        student.save()
    except User.DoesNotExist:
        return HttpResponse("User does not exist", status=404)

    return HttpResponse("Alexa id registered", status=200)


def check_user_exists(request, **kwargs):
    if kwargs["type"] == 'telegram':
        if Student.objects.filter(telegram_id=kwargs['id']).exists():
            return HttpResponse("Telegram id is registered", status=200)
        else:
            return HttpResponse("Telegram id is not registered", status=404)

    if kwargs["type"] == 'alexa':
        if Student.objects.filter(alexa_id=kwargs['id']).exists():
            return HttpResponse("Alexa id is registered", status=200)
        else:
            return HttpResponse("Alexa id is not registered", status=404)
