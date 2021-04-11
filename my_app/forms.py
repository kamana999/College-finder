from django import forms

from .models import *

class InserCity(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'


class InsertUni(forms.ModelForm):
    class Meta:
        model = University
        fields = '__all__'


class InsertCourse(forms.ModelForm):
    class Meta:
        model = CoursesName
        fields = '__all__'


class InsertCollege(forms.ModelForm):
    class Meta:
        model = College
        fields = '__all__'


class InsertStudent(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('doc',)


class InsertType(forms.ModelForm):
    class Meta:
        model = TypeName
        fields = '__all__'


class AddmissionForm(forms.ModelForm):

    studentid = forms.ModelChoiceField(queryset=Student.objects.all(),widget=forms.HiddenInput())
    college_id = forms.ModelChoiceField(queryset=College.objects.all(),widget=forms.HiddenInput())

    class Meta:
        model = Admission
        fields = '__all__'


class AddmissionF(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'


class LoginForm(forms.Form):
    email = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("comment", "rating")


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'


class RevForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("comment", "rating", "college")


