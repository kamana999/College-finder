from django.shortcuts import render, redirect
from .models import *
from django.views import generic
from django.db.models import Q, Count, Avg
from math import ceil
from .forms import *


def get_user(r):
    if r.session.has_key('login'):
        return Student.objects.get(email=r.session['login'])
    else:
        return {"username": "WHOO??"}


def login(r):
    form = LoginForm(r.POST or None)
    if r.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            cond = Q(email=username) & Q(password=password)
            check = Student.objects.get(cond)

            if check:
                r.session['login'] = username
                return redirect(index)
            else:
                return render(r, 'index.html')


def signup(r):
    form = InsertStudent(r.POST or None, r.FILES or None)
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(index)
    return render(r, 'index.html', {
        'signup_form': InsertStudent
    })


def logout(r):
    del r.session['login']
    return redirect(index)


def index(r):
    type = College.objects.all()
    n = len(type)
    nSlides = n//4 + ceil((n/4)-(n//4))
    review = Review.objects.all()
    average = review.aggregate(Avg("rating"))['rating__avg']
    if average == None:
        average = 0
    average = round(average, 2)
    return render(r, 'index.html', {
        'college':type,
        'category': CategoryName.objects.all(),
        'course': CoursesName.objects.all(),
        'type': TypeName.objects.all(),
        'addmissionn': AddmissionForm,
        'signup_form': InsertStudent,
        'login_form': LoginForm,
        'students': Student.objects.all().count(),
        'user': get_user(r),
        'coll': College.objects.all().count(),
        'cour': CoursesName.objects.all().count(),
        'average':average,
        'no_of_slides': nSlides,
        'range': range(1, nSlides),
    })


def course(r, cat_id):
    return render(r, 'index.html', {
        'course': CoursesName.objects.filter(course_cat=cat_id),
        'category': CategoryName.objects.all(),

    })


def cat(r, course_id):
        return render(r, 'cat.html', {
            'category': CategoryName.objects.all(),
            'course': CoursesName.objects.all().order_by("course_title"),
            'type': TypeName.objects.all(),
            'addmissionn': AddmissionForm,
            'colleges': College.objects.filter(course__courseId__course_id=course_id),
            'signup_form': InsertStudent,
            'login_form': LoginForm,
            'user': get_user(r),
            'states':State.objects.all(),
        })


def college(r):
    return render(r, 'college.html', {
        'category': CategoryName.objects.all(),
        'course': CoursesName.objects.all().order_by("course_title"),
        'colleges': College.objects.all(),
        'signup_form': InsertStudent,
        'login_form': LoginForm,
        'user': get_user(r),
        'states':State.objects.all()
    })


def addmission(r):
    log = r.session['login']
    std = Student.objects.get(email=log).s_id
    cond = Q(student=std) & Q(addmission_status=0)

    if not r.session.has_key('login'):
        return redirect(view)

    data = {
        "addm": AddmissionForm(cond),
        "student": Student.objects.filter(s_id=std),
        "studentadd": Admission.objects.filter(student=std)
    }
    std = Student.objects.filter(email=log)
    addm = AddmissionForm(r.POST or None)
    if r.method == "POST":
        if addm.is_valid():
            addm.save()
            return redirect(addmission)
    return render(r, 'view.html', data)


def view(r, college_id):
   if r.session.has_key('login'):
        log = r.session['login']
        review = Review.objects.filter(college=college_id).order_by("comment")
        average = review.aggregate(Avg("rating"))['rating__avg']
        if average ==None:
            average = 0
        average = round(average, 2)

        return render(r, 'view.html', {
            'college': College.objects.get(pk=college_id),
            'releted_college': College.objects.exclude(pk=college_id),
            'signup_form': InsertStudent,
            'login_form': LoginForm,
            'user': get_user(r),
            'addm': AddmissionForm(),
            'category': CategoryName.objects.all(),
            'course': CoursesName.objects.all(),
            'reviews': review,
            'log': log,
            'average': average,
        })
   else:
       review = Review.objects.filter(college=college_id).order_by("comment")
       average = review.aggregate(Avg("rating"))['rating__avg']
       if average == None:
           average = 0
       average = round(average, 2)
       return render(r, 'view.html', {
           'college': College.objects.get(pk=college_id),
           'releted_college': College.objects.exclude(pk=college_id),
           'signup_form': InsertStudent,
           'login_form': LoginForm,
           'user': get_user(r),
           'addm': AddmissionForm(),
           'category': CategoryName.objects.all(),
           'course': CoursesName.objects.all(),
           'reviews': review,
           'average': average,
       })


def dashboard(r):
    return render(r, 'dashboard.html', {
        'students': Student.objects.all().count(),
        'college': College.objects.all().count(),
        'course': CoursesName.objects.all().count()
    })


def insert(r):
    form = InsertCollege(r.POST or None, r.FILES or None)
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(insert)
    return render(r, 'insert.html', {
            'form': InsertCollege,
            'city': InserCity
        })


def search(r):
    if r.method == "GET":
        search = r.GET.get('search')
        return render(r, 'search.html', {
            'college': College.objects.filter(college_name__icontains=search),
            'course': CoursesName.objects.all(),
            'category': CategoryName.objects.all(),
            'signup_form': InsertStudent,
            'login_form': LoginForm,
            'user': get_user(r),
        })
    else:
        return redirect(index)


def add(r):
    form = AddmissionF(r.POST or None)
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(add)
    return render(r, 'add.html', {
        'add': AddmissionF()
    })


def add_review(r, college_id):
    if r.session.has_key('login'):
        college = College.objects.get(college_id=college_id)
        if r.method == "POST":
            form = ReviewForm(r.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = r.POST["comment"]
                data.rating = r.POST["rating"]
                data.student = Student.objects.get(email=r.session['login'])
                data.college = college
                data.save()
                return redirect(view, college_id)
        else:
            form = ReviewForm()
        return render(r, 'view.html', {
            'form': form,
        })
    else:
        return redirect(view, college_id)


def edit_review(r, college_id, review_id):
    if r.session.has_key('login'):
        college = College.objects.get(college_id=college_id)
        review = Review.objects.get(college=college, id=review_id)
        log = r.session['login']

        if r.method == "POST":
            if log == review.student.email:
                form = ReviewForm(r.POST, instance=review)
                if form.is_valid():
                    data = form.save(commit=False)
                    if (data.rating > 10) or (data.rating < 0):
                        error = "Out of range from 0 to 10"
                        return render(r, 'edit_review.html', {
                            'error': error,
                            'form': form
                        })
                    else:
                        data.save()
                        return redirect(view, college_id)
        else:
            form = ReviewForm(instance=review)
            return render(r, 'edit_review.html', {
                'form': form,

            })
    else:
        return redirect(view, college_id)


def del_review(r, college_id, review_id):
    if r.session.has_key('login'):
        college = College.objects.get(college_id=college_id)
        review = Review.objects.get(college=college, id=review_id)
        log = r.session['login']

        if log == review.student.email:
            review.delete()

        return redirect(view, college_id)
    else:
        return redirect(view, college_id)


def exam(r):
    return render(r, 'exam.html', {
        'category': CategoryName.objects.all(),
        'colleges': College.objects.all(),
        'signup_form': InsertStudent,
        'login_form': LoginForm,
        'user': get_user(r),
        'exams': Exam.objects.all().order_by("date_of_exam"),
        'examcourses': ExamCourse.objects.all(),
        'examcolleges': ExamCollege.objects.all(),

    })


def exam_cat(r, cat_id):
    return render(r, 'exam_cat.html', {
        'category': CategoryName.objects.all(),
        'category_name': CategoryName.objects.get(pk=cat_id),
        'exams': Exam.objects.filter(examcourse__category__cat_id=cat_id),
        'exam_cat': ExamCourse.objects.filter(category=cat_id),
        'signup_form': InsertStudent,
        'login_form': LoginForm,
        'user': get_user(r)
    })


def exam_view(r, e_id):
    return render(r, 'exam_view.html', {
        'exams': Exam.objects.get(pk=e_id),
        'signup_form': InsertStudent,
        'login_form': LoginForm,
        'user': get_user(r),
        'category': CategoryName.objects.all(),
        'course': CoursesName.objects.all(),
        'addm': AddmissionForm(),
    })


def search_course(r):
   if r.method == "GET":
       course = r.GET.get('course')
       return render(r, 'cat.html',  {
           'colleges': College.objects.filter(course__courseId__course_title__icontains=course),
           'category': CategoryName.objects.all(),
           'course': CoursesName.objects.all().order_by("course_title"),
           'signup_form': InsertStudent,
           'login_form': LoginForm,
           'user': get_user(r),
           'states': State.objects.all(),
       })
   else:
       return redirect(college)


def search_state(r):
    if r.method == "GET":
        state = r.GET.get('state')
        return render(r, 'cat.html', {
            'colleges': College.objects.filter(statecollege__state__state_name__icontains=state),
            'category': CategoryName.objects.all(),
            'course': CoursesName.objects.all().order_by("course_title"),
            'signup_form': InsertStudent,
            'login_form': LoginForm,
            'user': get_user(r),
            'states': State.objects.all(),
        })
    else:
        return redirect(college)


def state(r, s_id):
    return render(r, 'cat.html', {
        'category': CategoryName.objects.all(),
        'course': CoursesName.objects.all().order_by("course_title"),
        'type': TypeName.objects.all(),
        'addmissionn': AddmissionForm,
        'colleges': College.objects.filter(statecollege__state__id=s_id),
        'signup_form': InsertStudent,
        'login_form': LoginForm,
        'user': get_user(r),
        'states': State.objects.all(),
    })


def course_page(r):
    return render(r, 'course.html', {
        'category': CategoryName.objects.all(),
        'course': CoursesName.objects.all(),
        'signup_form': InsertStudent,
        'login_form': LoginForm,
        'user': get_user(r),
        'course_page': Category.objects.all()
    })


def course_view(r, cat_id):
    return render(r, 'course_view.html', {
        'category': CategoryName.objects.all(),
        'category_name': CategoryName.objects.get(pk=cat_id),
        'course': CoursesName.objects.filter(category__categoryId__cat_id=cat_id),
    })


def review(r):
    return render(r, 'review.html',{
        'reviews':Review.objects.all().order_by("rating"),
        'signup_form': InsertStudent,
        'login_form': LoginForm,
        'user': get_user(r),
        'category': CategoryName.objects.all(),
        'course': CoursesName.objects.all(),
        'rev': RevForm

    })


def rev(r):
        form = RevForm(r.POST or None)
        if r.method == "POST":
            if form.is_valid():
                data = form.save(commit=False)
                data.student = Student.objects.get(email=r.session['login'])
                data.save()
                return redirect(review)
        return render(r, 'review.html', {
            'rev': RevForm
        })


def addmission_page(r):
    return render(r, 'addmission.html', {
        'college': College.objects.all(),
        'signup_form': InsertStudent,
        'login_form': LoginForm,
        'user': get_user(r),
        'category': CategoryName.objects.all(),
        'course': CoursesName.objects.all(),
        'addm': AddmissionForm(),
    })




