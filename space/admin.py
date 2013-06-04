# -*- coding: utf-8 -*-

from django.contrib import admin
from space.models import *

admin.site.register(News,NewsAdmin)
admin.site.register(Member)
admin.site.register(Bussiness_Support)