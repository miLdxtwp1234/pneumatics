import secrets
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from PnHyWeb.models import ReportScore, Role, Student
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
import pdb


def home(request):
    return render(request,'homepage.html')
    
def index(request):
    return render(request,'login.html')

def register(request):
   return render(request,'register.html')

def competency(request):
    return render(request, 'competency.html')

def unit1(request):
    return render(request, 'unit1.html')

def unit2(request):
    return render(request, 'unit2.html')

def unit3(request):
    return render(request, 'unit3.html')

def test(request):
    return render(request, 'test.html')

def pretest(request):
    return render(request, 'pretest.html')

def posttest(request):
    return render(request, 'posttest.html')

def studentReport(request):
    return render(request, 'studentReport.html')

def worksheet(request):
    return render(request, 'worksheet.html')

@csrf_exempt
def register_post(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id') 
        if Student.objects.filter(student_id=student_id).exists():
            error_message = "Student ID already exists"
            return render(request, 'register.html', {'error_message': error_message})

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        token = secrets.token_urlsafe(255)
        if student_id == '' or first_name == '' or last_name == '' or email == '' or password == '' or confirm_password == '':
            error_message = "Please fill in complete information."
            return render(request, 'register.html', {'error_message': error_message})
        if password != confirm_password:
            error_message = "Passwords do not match"
            return render(request, 'register.html', {'error_message': error_message})
        if len(password) < 8:  
            error_message = "Password must be at least 8 characters long"
            return render(request, 'register.html', {'error_message': error_message})

        # Retrieve the role object for 'student'
        student_role = Role.objects.get(role_id='2')

        # Create the student object with the retrieved role object
        student = Student(student_id=student_id, password=password, email=email, first_name=first_name, last_name=last_name, token=token, role=student_role)
        student.save()
        success_message = "Register Successful"
        return render(request, 'register.html', {'success_message' : success_message, 'token' : token})
    else:
        return HttpResponse("Only POST requests are allowed", status=405)

    

@csrf_exempt
def postLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =  Student.objects.filter(student_id=username).first() \
                or Student.objects.filter(email=username).first()
        if user.password == password:
            token = secrets.token_urlsafe(255)
            user.token = token
            user.save()
            return JsonResponse({'sucess' : 'Login Sucessfully', 'token' : token})
        else:
            return JsonResponse(status=401)
    else :
        return HttpResponse("Only POST requests are allowed", status=405)
    
@csrf_exempt
def postLogout(request):
    if request.method == 'POST':
        token = request.POST.get('token')
        user = Student.objects.filter(token=token).first()
        if user:
            if user.token:
                user.token = ''
                user.save()
    
@csrf_exempt
def get_user(request):
    # pdb.set_trace() ไว้ Debugger
    if request.method == 'POST':
        token = request.POST.get('token')
        if Student.objects.filter(token=token).exists():
            user = Student.objects.get(token=token)
            first_name = user.first_name
            last_name = user.last_name
            return JsonResponse({'first_name': first_name, 'last_name': last_name})
    else:
        return HttpResponse("Only POST requests are allowed", status=405)

@csrf_exempt
def postPretest(request):
    if request.method == 'POST':
        token = request.POST.get('token')
        pretest_score = request.POST.get('pretest')
        if Student.objects.filter(token=token).exists():
            student_search = Student.objects.get(token=token)
            student_save = ReportScore(student_id=student_search.student_id, pre_test=pretest_score)
            student_save.save()
            return HttpResponse("Pretest score saved successfully")  


    return HttpResponse("Invalid request or student not found")

@csrf_exempt
def postPosttest(request):
    if request.method == 'POST':
        token = request.POST.get('token')
        posttest_score = request.POST.get('pretest')
        if Student.objects.filter(token=token).exists():
            student_search = Student.objects.get(token=token).student_id
            student_pretest = ReportScore.objects.get(student_id = student_search).pre_test
            student_save = ReportScore(student_id=student_search, pre_test = student_pretest, post_test=posttest_score)
            student_save.save()
            return HttpResponse("Pretest score saved successfully")  
    return HttpResponse("Invalid request or student not found")

@csrf_exempt
def get_student_report(request):

    if request.method == "GET":
        # Fetching student and their report scores
        students_with_scores = []
        for student in Student.objects.all():
            try:
                report_score = ReportScore.objects.get(student=student)
                students_with_scores.append({
                    'student_id': student.student_id,
                    'first_name': student.first_name,
                    'last_name': student.last_name,
                    'pre_test': report_score.pre_test,
                    'post_test': report_score.post_test,
                })
            except ReportScore.DoesNotExist:
                students_with_scores.append({
                    'student_id': student.student_id,
                    'first_name': student.first_name,
                    'last_name': student.last_name,
                    'pre_test': None,
                    'post_test': None,
                })
                
        return JsonResponse({'student_data' : students_with_scores})




if not Role.objects.filter(role_id=Role.TEACHER).exists():
    teacher_role = Role.objects.create(role_id=Role.TEACHER, role_name='Teacher')
    teacher_role.save()

if not Role.objects.filter(role_id=Role.STUDENT).exists():
    student_role = Role.objects.create(role_id=Role.STUDENT, role_name='Student')
    student_role.save()