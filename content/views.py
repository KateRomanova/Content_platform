from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from content.forms import ContentForm
from content.models import Content
from users.services import check_payment_status


class ContentListView(ListView):
    model = Content

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['is_paid'] = check_payment_status(self.request.user)
        else:
            context['is_paid'] = False
        print(context['is_paid'])
        return context


class ContentDetailView(UserPassesTestMixin, DetailView):
    model = Content

    def test_func(self):
        if not self.request.user.is_authenticated and self.get_object().is_content_paid:
            return False
        elif not self.request.user.is_authenticated and not self.get_object().is_content_paid:
            return True
        elif self.request.user.is_authenticated and self.get_object().owner == self.request.user:
            return True
        elif not check_payment_status(self.request.user) and self.get_object().is_content_paid:
            return False
        return True


class ContentCreateView(CreateView, LoginRequiredMixin):
    model = Content
    form_class = ContentForm
    success_url = reverse_lazy("content:content_list")

    def form_valid(self, form):
        content = form.save()
        user = self.request.user
        content.owner = user
        content.save()
        return super().form_valid(form)


class ContentUpdateView(UserPassesTestMixin, UpdateView):
    model = Content
    form_class = ContentForm
    success_url = reverse_lazy("content:content_list")

    def test_func(self):
        if not self.request.user.is_authenticated and self.get_object().is_content_paid:
            return False
        elif not self.request.user.is_authenticated and not self.get_object().is_content_paid:
            return True
        elif self.request.user.is_authenticated and self.get_object().owner == self.request.user:
            return True
        elif not check_payment_status(self.request.user) and self.get_object().is_content_paid:
            return False
        return True


class ContentDeleteView(UserPassesTestMixin, DeleteView):
    model = Content
    success_url = reverse_lazy("content:content_list")

    def test_func(self):
        if not self.request.user.is_authenticated and self.get_object().is_content_paid:
            return False
        elif not self.request.user.is_authenticated and not self.get_object().is_content_paid:
            return True
        elif self.request.user.is_authenticated and self.get_object().owner == self.request.user:
            return True
        elif not check_payment_status(self.request.user) and self.get_object().is_content_paid:
            return False
        return True
