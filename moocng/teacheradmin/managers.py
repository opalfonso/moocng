# -*- coding: utf-8 -*-
# Copyright 2012-2013 Rooter Analysis S.L.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.db import models


class MassiveEmailManager(models.Manager):

    """
    Manager function for mass amil sending when the teacher creates an announcement
    in the course.

    .. versionadded:: 0.1
    """
    def create_from_announcement(self, announcement):
        return super(MassiveEmailManager, self).create(
            course=announcement.course,
            datetime=announcement.datetime,
            subject=announcement.title,
            message=announcement.content,
        )
