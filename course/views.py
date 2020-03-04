
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from braces.views import LoginRequiredMixin,CsrfExemptMixin,JsonRequestResponseMixin
from .models import Course
from .forms import CreateCourseForm



# Create your views here.

class AboutView(TemplateView):
    template_name = 'course/about.html'

class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'course/course_list.html'



class ManageCourseListView(LoginRequiredMixin,ListView):
    model = Course
    login_url = '/account/login/'
    context_object_name = 'courses'
    template_name = "course/manage/manage_course_list.html"

    def get_queryset(self):
        qs = super(ManageCourseListView, self).get_queryset()
        return qs.filter(user=self.request.user)

class CreateCourseView(LoginRequiredMixin,CreateView):
    model = Course
    login_url = '/account/login/'
    context_object_name = 'courses'
    fields = ['title', 'overview']
    template_name = 'course/manage/create_course.html'

    def get_queryset(self):
        qs = super(CreateCourseView, self).get_queryset()
        return qs.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        form = CreateCourseForm(data=request.POST)
        if form.is_valid():
            new_course = form.save(commit=False)
            new_course.user = self.request.user
            new_course.save()
            return redirect("course:manage_course")


