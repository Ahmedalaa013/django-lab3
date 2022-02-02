from django.shortcuts import render,redirect
from student.models import Student


def delete_student(request, id):
     student = Student.objects.get(pk=id)
     student.delete()
     return redirect('home')
    


def create_student(request):
    if request.method == 'POST':
        name = request.POST.get('student_name')
        Student.objects.create(name=name)
    return redirect('home')


def update_student(request, id):
        name = request.POST.get('student_name')
        record = Student.objects.get(id=id)
        if record:
            print(record.name, "1st")
            record.name = name
            print(record.name, "2nd")
            record.save()
            return redirect('home')
        


def select_student(request):  
    context = {'student_select': Student.objects.all()}
    return render(request, "user/home.html",context)
        
