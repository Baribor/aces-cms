from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    salary = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        abstract = True


class Patient(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(blank=True, null=True, max_length=100)
    gender = models.CharField(blank=False, null=False, max_length=6, choices=(("Male","Male"), ("Female", "Female")))
    phone = models.CharField(blank=True, null=True, max_length=15)

    class Meta:
        db_table = "User"


class Doctor(Staff):
    qualification = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        db_table = "Doctor"

class Nurse(Staff):
    class Meta:
        db_table = "Nurse"

class Pharmacist(Staff):
    class Meta:
        db_table = "Pharmacist"

class LabAssistant(Staff):
    class Meta:
        db_table = "LabAssistant"


class Receptionist(Staff):
    class Meta:
        db_table = "Receptionist"


class Cashier(Staff):
    class Meta:
        db_table = "Cashier"


class Medicine(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    quantity = models.IntegerField()

    class Meta:
        db_table = "Medicine"

class Appointment(models.Model):
    date = models.DateTimeField(auto_now=True)
    doctorId = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    nurseId = models.ForeignKey(Nurse, on_delete=models.SET_NULL, null=True)
    patientId = models.ForeignKey(Patient, on_delete=models.CASCADE)

    class Meta:
        db_table = "Appointment"


class Bill(models.Model):
    time = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    cashierId = models.ForeignKey(Cashier, on_delete=models.SET_NULL, null=True)
    patientId = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "Bill"

class Prescription(models.Model):
    patientId = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    doctorId = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    pharmacistId = models.ForeignKey(Pharmacist, on_delete=models.CASCADE, null=True)
    medicines = models.ManyToManyField(Medicine)
    date = models.DateField(auto_now=True)

    class Meta:
        db_table = "Prescription"


class LabResult(models.Model):
    patientId = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, verbose_name="Patient ID")
    labAssistantId = models.ForeignKey(LabAssistant, on_delete=models.CASCADE, null=True, verbose_name="Lab assist. ID")
    description = models.TextField()
    date = models.DateField(auto_now=True)

    class Meta:
        db_table = "LabResult"