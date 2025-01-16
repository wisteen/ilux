# Generated by Django 4.2 on 2025-01-12 21:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('full_name', models.CharField(max_length=255, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Country')),
                ('face_encoding', models.TextField(blank=True, help_text='Stores face encoding data', null=True)),
                ('email_verification_token', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff Status')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Superuser Status')),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_set', to='auth.group', verbose_name='Groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_user_set', to='auth.permission', verbose_name='User Permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ['-date_joined'],
            },
        ),
    ]
