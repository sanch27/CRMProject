# Generated by Django 5.0.2 on 2024-02-29 09:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_courses_packages_packageoptions_subscriptions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('package_id', models.AutoField(primary_key=True, serialize=False)),
                ('package_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name='packageoptions',
            name='CourseID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.course'),
        ),
        migrations.AlterField(
            model_name='packageoptions',
            name='PackageID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.package'),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('subscription_id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_date', models.DateTimeField()),
                ('expiry_date', models.DateTimeField()),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.package')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Subscriptions',
        ),
        migrations.DeleteModel(
            name='Courses',
        ),
        migrations.DeleteModel(
            name='Packages',
        ),
    ]
