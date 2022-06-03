# Generated by Django 4.0.3 on 2022-05-28 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_alter_lab_l_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('c_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('lab_n', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.lab')),
            ],
        ),
    ]
