# Generated by Django 5.0.6 on 2024-07-12 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MIS', '0007_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userbase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
