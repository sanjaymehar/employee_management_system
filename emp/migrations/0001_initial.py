# Generated by Django 4.0.4 on 2022-10-08 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('IT', 'IT'), ('ACCOUNTS', 'ACCOUNTS')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('ACCEPTED', 'ACCEPTED'), ('COMPLETED', 'COMPLETED')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp.department')),
                ('salary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp.salary')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp.task')),
            ],
        ),
    ]
