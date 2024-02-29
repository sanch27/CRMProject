from django.contrib import admin
from .models import Record, Course, Package,PackageOptions, Subscription

admin.site.register(Record)
admin.site.register(Course)
admin.site.register(Package)
admin.site.register(PackageOptions)
admin.site.register(Subscription)


