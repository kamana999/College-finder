from django.db import models
from django.utils import timezone
from datetime import datetime


class State(models.Model):
    state_name = models.CharField(max_length=200)

    def __str__(self):
        return self.state_name


class City(models.Model):
    city_name = models.CharField(max_length=200)
    state_name = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name


class TypeName(models.Model):
    type_id = models.AutoField(primary_key=True)
    course_type = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.course_type


class University(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=200)
    u_icon = models.ImageField(upload_to='pic/', null=True, blank=True)

    def __str__(self):
        return self.u_name


class CategoryName(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=200)
    cat_icon = models.ImageField(upload_to='pic/', null=True, blank=True)

    def __str__(self):
        return self.cat_name


class CoursesName(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_title = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200)
    course_duration = models.CharField(max_length=200)
    course_fee = models.IntegerField(default=0)
    elegibilty = models.CharField(max_length=200)
    course_type = models.ForeignKey(TypeName, on_delete=models.CASCADE)
    course_cat = models.ForeignKey(CategoryName, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.course_name


class Category(models.Model):
    ca_id = models.AutoField(primary_key=True)
    categoryId = models.ForeignKey(CategoryName, on_delete=models.CASCADE)
    courseeId = models.ForeignKey(CoursesName, on_delete=models.CASCADE)

    def __str__(self):
        return self.courseeId.course_title


class College(models.Model):
    college_id = models.AutoField(primary_key=True)
    college_name = models.CharField(max_length=200)
    affiliated_to = models.ForeignKey(University, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    phone = models.IntegerField()
    img = models.ImageField(upload_to='pic/')
    website = models.URLField()
    desc = models.TextField(blank=True)
    avgrating = models.FloatField(default=0)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.college_name


class Student(models.Model):
    s_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=200)
    contact = models.IntegerField()
    email = models.EmailField(unique=True)
    dp = models.ImageField(upload_to="pic/")
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    dob = models.DateField()
    status = models.IntegerField(default=0)
    password = models.CharField(max_length=200)
    doc = models.DateField()

    def __str__(self):
        return self.student_name


class Review(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.student.student_name


class Type(models.Model):
    t_id = models.AutoField(primary_key=True)
    type = models.ForeignKey(TypeName, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.type.course_type


class Course(models.Model):
    c_id = models.AutoField(primary_key=True)
    courseId = models.ForeignKey(CoursesName, on_delete=models.CASCADE)
    collegeId = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.collegeId.college_name


class Admission(models.Model):

    a_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    course = models.ForeignKey(CoursesName, on_delete=models.CASCADE)
    addmission_status = models.IntegerField(default=0)

    def __str__(self):
        return self.student.student_name


class Exam(models.Model):
    e_id = models.AutoField(primary_key=True)
    exam_title = models.CharField(max_length=200)
    exam_name = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    date_of_exam = models.DateField()
    doc = models.DateTimeField(default=timezone.now)
    exam_eligiblity = models.TextField(max_length=2000)
    age_limit = models.CharField(max_length=200)
    syllabus = models.TextField(max_length=1000)
    application_process = models.TextField(max_length=2000)
    application_fee = models.CharField(max_length=500)
    exam_center = models.CharField(max_length=1000)
    mobile = models.IntegerField()
    exam_website = models.URLField()
    office_address = models.CharField(max_length=500)
    exam_mode = models.CharField(max_length=200)
    exam_duration = models.CharField(max_length=300)
    application_date = models.DateTimeField(default=timezone.now)
    release_date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.exam_title


class ExamCourse(models.Model):
    ec_id = models.AutoField(primary_key=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryName, on_delete=models.CASCADE, default=None)


class ExamCollege(models.Model):
    eco_id = models.AutoField(primary_key=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)


class StateCollege(models.Model):
    s_id = models.AutoField(primary_key=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)









