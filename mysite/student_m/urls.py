from django.urls import path

from . import views

urlpatterns = [
    path('home/',views.home, name="home"),
    path('login/',views.login_view, name="login"),
    path('signup/',views.signup_view, name="signup"),
    path('form/',views.student_form,name='insert'),
    path('<int:id>/',views.student_form,name='update'),
    path('list/',views.student_list,name='list'),
    # path('update/',views.employee_list,name="update")
]
