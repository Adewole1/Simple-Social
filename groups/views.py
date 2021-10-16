from django.shortcuts import render

from django.http import HttpResponseRedirect

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages

from django.shortcuts import get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, RedirectView, DeleteView

from . import models
from . import forms

from .models import Group, GroupMember

from django.contrib.auth import get_user_model
User = get_user_model()

from braces.views import SelectRelatedMixin


class CreateGroup(LoginRequiredMixin, CreateView):
    model = Group
    form_class = forms.UserForm

    def form_valid(self, form, *args, **kwargs):
        group = form.save(commit=False)
        group.creator = self.request.user
        group.save()
        return HttpResponseRedirect(reverse('groups:join', kwargs={'slug': group.slug}))


class SingleGroup(DetailView):
    model = Group


class ListGroups(ListView):
    model = Group


class JoinGroup(LoginRequiredMixin, RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        except:
            messages.warning(self.request, 'Warning: Already A Member')
        else:
            messages.success(self.request, 'You are now  member')

        return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):

        try:
            membership = models.GroupMember.objects.filter(
                user = self.request.user,
                group__slug = self.kwargs.get('slug')
            ).get()
        except models.GroupMember.DoesNotExist:
            messages.warning(self.request, 'Warning: You are not a member')
        else:
            membership.delete()
            messages.success(self.request, 'You have left the group')

        return super().get(request, *args, **kwargs)


@login_required
def delete_group(request, slug):
    group = get_object_or_404(Group, slug=slug)
    group.delete()
    return redirect('groups:all')
