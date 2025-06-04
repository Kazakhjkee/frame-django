
from django.http import HttpResponse
from .models import Course, Student

def course_list(request):
    courses = Course.objects.all()
    return HttpResponse("<br>".join([course.hype() for course in courses]))

def student_list(request):
    students = Student.objects.all()
    return HttpResponse("<br>".join([student.motivation() for student in students]))

def general_info(request, type):
    if type == "courses":
        return course_list(request)
    elif type == "students":
        return student_list(request)
    return HttpResponse("Неизвестный тип")
