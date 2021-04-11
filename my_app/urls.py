from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('addmission/', views.addmission, name="addmission"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('category/<int:cat_id>', views.course, name="catname"),
    path('add/', views.add, name="add"),
    path('college/', views.college, name="college"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('search/', views.search, name="search"),
    path('<int:course_id>/cat/', views.cat, name="cat"),
    path('<int:s_id>/state/', views.state, name="state"),
    path('insert/', views.insert, name="insert"),
    path('rev/', views.rev, name="rev"),
    path('<int:college_id>/view/', views.view, name="view"),
    path('addreview/<int:college_id>/', views.add_review, name="addreview"),
    path('editreview/<int:college_id>/<int:review_id>', views.edit_review, name="edit_review"),
    path('delreview/<int:college_id>/<int:review_id>', views.del_review, name="del_review"),
    path('exam/', views.exam, name="exam"),
    path('exam_cat/<int:cat_id>', views.exam_cat, name="exam_cat"),
    path('exam_view/<int:e_id>', views.exam_view, name="exam_view"),
    path('search_course/', views.search_course, name="search_view"),
    path('search_state/', views.search_state, name="search_state"),
    path('course_page/', views.course_page, name="course_page"),
    path('course_view/<int:cat_id>', views.course_view, name="course_view"),
    path('review/', views.review, name="review"),
    path('addmission_page/', views.addmission_page, name="addmission_page")
]

