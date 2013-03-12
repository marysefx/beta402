# Copyright 2012, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from json import loads
from django.db import models
from users.models import Profile


class Course(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def last_info(self):
        data = self.courseinfo_set.all()[0]
        data.infos = loads(data.infos)
        return data


class CourseInfo(models.Model):
    user = models.ForeignKey(Profile)
    infos = models.TextField()
    date = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course)

    class Meta:
        ordering = ['-date']


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    sub_categories = models.ManyToManyField('self', symmetrical=False)
    contains = models.ManyToManyField(Course)
