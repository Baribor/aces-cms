from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("id","firstName", "lastName", "phone", "gender","occupation")

@admin.register(Church)
class ChurchAdmin(admin.ModelAdmin):
    list_display = ("id","name", "location", "description")

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("id","theme", "attendance", "guests", "date", "churchId")

@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ("id","amount", "memberId", "date")

@admin.register(Seed)
class SeedAdmin(admin.ModelAdmin):
    list_display = ("id","type", "amount", "memberId", "churchId", "description")

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("name", "churchId")

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=("name", "description", "churchId")

@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ("id", "topic", "speaker", "description")

@admin.register(ActivityDetail)
class ActivityDetailsAdmin(admin.ModelAdmin):
    list_display = ("attendance", "guests", "activity", "income", "date")