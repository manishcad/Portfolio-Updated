from django.contrib import admin
from .models import Projects, Certificate, Review, Tag
# Register your models here.

admin.site.register(Projects)
admin.site.register(Certificate)

admin.site.register(Review)

admin.site.register(Tag)
