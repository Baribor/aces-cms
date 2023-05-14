from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("id","name", "gender", "phone", "email")

@admin.register(LabAssistant)
class LabAssistantAdmin(admin.ModelAdmin):
    list_display = ("id","name", "salary")

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("id","name", "salary")

@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ("id","name", "salary")

@admin.register(Receptionist)
class ReceptionistAdmin(admin.ModelAdmin):
    list_display = ("id","name", "salary")

@admin.register(Cashier)
class CashierAdmin(admin.ModelAdmin):
    list_display = ("id","name", "salary")

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display=("name", "quantity")

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "doctorId", "nurseId", "patientId", "date")

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ("cashierId", "patientId", "amount", "time")

@admin.register(Pharmacist)
class PharmacistAdmin(admin.ModelAdmin):
    list_display = ("id","name", "salary")

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ("patientId", "doctorId", "pharmacistId", "date")

@admin.register(LabResult)
class LabResultAdmin(admin.ModelAdmin):
    list_display = ("patientId", "labAssistantId", "description", "date")