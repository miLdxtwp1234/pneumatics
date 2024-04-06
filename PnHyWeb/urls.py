from django.urls import path
from PnHyWeb import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# from .views import index
# from .views import register
# from .views import competency


urlpatterns = [
    path("",views.home, name='home'),
    path("login/" ,views.index, name='login'),
    path("register/" ,views.register, name='register'),
    path("competency/" ,views.competency, name='competency'),
    path("unit1/",views.unit1, name= 'unit1'),
    path("unit2/",views.unit2, name= 'unit2'),
    path("unit3/",views.unit3, name= 'unit3'),
    path("test/",views.test, name= 'test'),
    path("pretest/",views.pretest, name= 'pretest'),
    path("posttest/",views.posttest, name='posttest'),
    path('register/register_post', views.register_post, name='register_post'),
    path("getUser", views.get_user, name='getUser'),
    path('postLogin', views.postLogin, name="postLogin"),
    path('postLogout', views.postLogout, name="postLogout"),
    path('studentReportPost', views.get_student_report, name="studentReportPost"),
    path("studentReport", views.studentReport, name="studentReport"),
    path("pretestPost", views.postPretest, name="pretestPost"),
    path("postPosttest", views.postPosttest, name="postPosttest"),
    path("worksheet/", views.worksheet, name="worksheet"),
]