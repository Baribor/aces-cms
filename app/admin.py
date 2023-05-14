from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass

@admin.register(LabAssistant)
class LabAssistantAdmin(admin.ModelAdmin):
    pass

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    pass

@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    pass

@admin.register(Receptionist)
class ReceptionistAdmin(admin.ModelAdmin):
    pass

@admin.register(Cashier)
class CashierAdmin(admin.ModelAdmin):
    pass

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    pass

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    pass

@admin.register(Pharmacist)
class PharmacistAdmin(admin.ModelAdmin):
    pass

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    pass

@admin.register(LabResult)
class LabResultAdmin(admin.ModelAdmin):
    pass