# GROUPS MODELS

from django import template
from django.db import models
from django.utils.text import slugify

import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

register = template.Library()

class Group(models.Model):
    name = models.CharField(unique=True, max_length=50)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')
    creator = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self, *args, **kwargs):
        from django.urls import reverse
        return reverse('groups:join', kwargs={'slug': self.slug})


    class Meta:
        ordering = ['name']

class GroupMember(models.Model):
    group = models.ForeignKey("Group", related_name='memberships', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_groups', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')