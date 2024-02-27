from django.contrib import admin
from .models import Record, Courses, Packages, PackageOptions, Subscriptions

admin.site.register(Record)
admin.site.register(Courses)
admin.site.register(Packages)
admin.site.register(PackageOptions)
admin.site.register(Subscriptions)

