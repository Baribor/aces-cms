# Generated by Django 4.2.1 on 2023-05-13 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cashier',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'db_table': 'Cashier',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=6)),
                ('qualification', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Doctor',
            },
        ),
        migrations.CreateModel(
            name='LabAssistant',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'db_table': 'LabAssistant',
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
            ],
            options={
                'db_table': 'Medicine',
            },
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'db_table': 'Nurse',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(max_length=6)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Pharmacist',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'db_table': 'Pharmacist',
            },
        ),
        migrations.CreateModel(
            name='Receptionist',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'db_table': 'Receptionist',
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now=True)),
                ('doctorId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.doctor')),
                ('patientId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.patient')),
                ('pharmacistId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.pharmacist')),
            ],
            options={
                'db_table': 'Prescription',
            },
        ),
        migrations.CreateModel(
            name='LabResult',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now=True)),
                ('labAssistantId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.labassistant')),
                ('patientId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.patient')),
            ],
            options={
                'db_table': 'LabResult',
            },
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('cashierId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.cashier')),
                ('patientId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.patient')),
            ],
            options={
                'db_table': 'Bill',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('doctorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.doctor')),
                ('nurseId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.nurse')),
                ('patientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.patient')),
            ],
            options={
                'db_table': 'Appointment',
            },
        ),
    ]