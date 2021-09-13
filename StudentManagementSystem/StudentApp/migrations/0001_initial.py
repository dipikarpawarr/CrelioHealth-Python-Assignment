# Generated by Django 3.2.5 on 2021-09-08 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Assignment_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AssignmentName', models.CharField(max_length=100)),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('AddedBy', models.CharField(max_length=100)),
                ('AddedDate', models.DateField()),
            ],
            options={
                'db_table': 'Assignment',
            },
        ),
        migrations.CreateModel(
            name='Assignment_Marks_Model',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Marks', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'Assignment_Marks',
            },
        ),
        migrations.CreateModel(
            name='Class_Model',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Class', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'Class',
            },
        ),
        migrations.CreateModel(
            name='Login_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=40)),
                ('Password', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'Login',
            },
        ),
        migrations.CreateModel(
            name='Stud_Registration_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=100)),
                ('MiddletName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Unisex', 'Unisex/Parody')], max_length=6)),
                ('Pincode', models.CharField(max_length=6)),
                ('MobileNumber', models.CharField(max_length=10)),
                ('ParentName', models.CharField(max_length=100)),
                ('Occupation', models.CharField(max_length=50)),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentApp.class_model')),
            ],
            options={
                'db_table': 'Registration',
            },
        ),
        migrations.CreateModel(
            name='Fill_Assignment_Report_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AddedBy', models.CharField(max_length=100)),
                ('AddedDate', models.DateField()),
                ('Assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentApp.add_assignment_model')),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentApp.class_model')),
                ('Marks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentApp.assignment_marks_model')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentApp.stud_registration_model')),
            ],
            options={
                'db_table': 'Fill_Assignment_Report',
            },
        ),
        migrations.AddField(
            model_name='add_assignment_model',
            name='Class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentApp.class_model'),
        ),
    ]