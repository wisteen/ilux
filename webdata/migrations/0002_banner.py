# Generated by Django 4.2 on 2025-01-12 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('discount_percentage', models.PositiveIntegerField(blank=True, null=True)),
                ('button_label', models.CharField(blank=True, max_length=50, null=True)),
                ('button_link', models.URLField(blank=True, max_length=500, null=True)),
                ('background_image', models.ImageField(upload_to='banners/')),
                ('background_position', models.CharField(choices=[('center', 'Center'), ('top', 'Top'), ('bottom', 'Bottom'), ('left', 'Left'), ('right', 'Right')], default='center', max_length=50)),
                ('background_size', models.CharField(choices=[('cover', 'Cover'), ('contain', 'Contain')], default='cover', max_length=50)),
                ('background_repeat', models.BooleanField(default=False)),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
