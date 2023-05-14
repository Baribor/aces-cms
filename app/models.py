from django.db import models


class Church(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    location = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "Church"
        constraints = [
            models.UniqueConstraint(fields=["name","location"], name="Unique church")
        ]
        verbose_name_plural = "Churches"


class Event(models.Model):
    theme = models.CharField(max_length=255)
    attendance = models.IntegerField()
    guests = models.IntegerField()
    churchId = models.ForeignKey(Church, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)


    def __str__(self) -> str:
        return self.theme
    
    class Meta:
        db_table = "Event"


class Member(models.Model):
    firstName = models.CharField(max_length=100, blank=False, null=False)
    lastName = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=6, choices=(("Male", "Male"), ("Female", "Female")), blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    churchId = models.ForeignKey(Church, on_delete=models.CASCADE)
    departments = models.ManyToManyField("Department")

    def __str__(self) -> str:
        return f"{self.firstName} {self.lastName}"
    
    class Meta:
        db_table = "Member"


class Payroll(models.Model):
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    memberId = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)


    def __str__(self) -> str:
        return f"payroll - {self.memberId}"
    
    class Meta:
        db_table = "Payroll"


class Seed(models.Model):
    type = models.CharField(max_length=15, choices=(("Offering", "Offering"), ("Tithe", "Tithe"), ("Project", "Project"), ("Others", "Others")), blank=False, null=False)
    description = models.TextField()
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    churchId = models.ForeignKey(Church, on_delete=models.CASCADE)
    memberId = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"Seed - {self.type}"
    
    class Meta:
        db_table = "Seed"

class Activity(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    churchId = models.ForeignKey(Church, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = "Activity"
        verbose_name_plural = "Activities"

class Department(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    description = models.TextField()
    churchId = models.ForeignKey(Church, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = "Department"


class ActivityDetail(models.Model):
    attendance = models.IntegerField()
    guests = models.IntegerField(default=0)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    income = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"ActivityDetail - {self.activity}"
    
    class Meta:
        db_table = "ActivityDetails"

class Sermon(models.Model):
    topic = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    speaker = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    details = models.ForeignKey(ActivityDetail, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.topic
    
    class Meta:
        db_table = "Sermon"