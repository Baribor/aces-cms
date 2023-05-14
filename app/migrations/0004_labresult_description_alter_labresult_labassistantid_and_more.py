# Generated by Django 4.2.1 on 2023-05-13 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_prescription_medicines'),
    ]

    operations = [
        migrations.AddField(
            model_name='labresult',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='labresult',
            name='labAssistantId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.labassistant', verbose_name='Lab assist. ID'),
        ),
        migrations.AlterField(
            model_name='labresult',
            name='patientId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.patient', verbose_name='Patient ID'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6),
        ),
    ]
