from django.urls import path
from .views import *


urlpatterns = [
    path('index/',index),
    path("add_book/", add_book),
    path("view_books/",view_books),
    path("view_students/",view_students),
    path("issue_book/",issue_book),
    path("view_issued_book/",view_issued_book),
    path("view_issued_bookstudent/",view_issued_bookstudent),

    path("student_issued_books/",student_issued_books),
    path("profile/", profile,),
    path("edit_profile/",edit_profile),

    path("student_registration/",student_registration),
    path("change_password/",change_password),
    path("student_login/",student_login),
    path("admin_login/", admin_login),
    path("logout/",Logout),

    path("delete_book/<int:myid>/",delete_book),
    path("delete_student/<int:myid>/",delete_student),
    path("delete_issue/<int:myid>",delete_issue)

]