from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import RunningActivityForm
from .models import RunningActivity


class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy('logged-out')


class LoggedOutView(TemplateView):
    template_name = 'logged_out.html'


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


class RunningActivityCreateView(LoginRequiredMixin, CreateView):
    model = RunningActivity
    form_class = RunningActivityForm
    success_url = reverse_lazy('activity-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RunningActivityDeleteView(LoginRequiredMixin, DeleteView):
    model = RunningActivity
    success_url = reverse_lazy('activity-list')

    def get_queryset(self):
        return RunningActivity.objects.filter(user=self.request.user)


class RunningActivityListView(LoginRequiredMixin, ListView):
    model = RunningActivity
    template_name = 'leaderboards/activity_list.html'
    context_object_name = 'activities'

    def get_queryset(self):
        return RunningActivity.objects.filter(user=self.request.user)


class RunningActivityUpdateView(LoginRequiredMixin, UpdateView):
    model = RunningActivity
    form_class = RunningActivityForm
    success_url = reverse_lazy('activity-list')

    def get_queryset(self):
        return RunningActivity.objects.filter(user=self.request.user)
