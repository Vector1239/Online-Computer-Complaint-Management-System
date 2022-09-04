# Generated by Django 4.0.3 on 2022-05-30 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_computer_c_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('r_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('r_mouse', models.IntegerField(null=True)),
                ('r_keyboard', models.IntegerField(null=True)),
                ('r_monitor', models.IntegerField(null=True)),
                ('r_OS', models.IntegerField(null=True)),
                ('r_internet', models.IntegerField(null=True)),
                ('r_other', models.CharField(max_length=200, null=True, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('comp_n', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.computer')),
                ('std_mail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.student')),
            ],
        ),
    ]