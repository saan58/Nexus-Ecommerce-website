# Generated by Django 5.0 on 2024-01-03 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_signup'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='confirmPassword',
            field=models.CharField(default='newPassword', max_length=122),
        ),
    ]