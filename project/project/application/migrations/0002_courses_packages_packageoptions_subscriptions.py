# Generated by Django 5.0.2 on 2024-02-27 15:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('CourseID', models.AutoField(primary_key=True, serialize=False)),
                ('CourseName', models.CharField(max_length=255)),
                ('CourseDescription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('PackageID', models.AutoField(primary_key=True, serialize=False)),
                ('PackageName', models.CharField(max_length=255)),
                ('PackageDescription', models.TextField()),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='PackageOptions',
            fields=[
                ('OptionID', models.AutoField(primary_key=True, serialize=False)),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.courses')),
                ('PackageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.packages')),
            ],
        ),
        migrations.CreateModel(
            name='Subscriptions',
            fields=[
                ('SubscriptionID', models.AutoField(primary_key=True, serialize=False)),
                ('PaymentDate', models.DateField()),
                ('ExpiryDate', models.DateField()),
                ('PackageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.packages')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
