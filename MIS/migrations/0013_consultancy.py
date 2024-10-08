# Generated by Django 5.0.7 on 2024-07-31 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MIS', '0012_offline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceProvider', models.CharField(max_length=500)),
                ('orderFileNo', models.CharField(max_length=50)),
                ('orderDated', models.DateField()),
                ('serviceStartDate', models.DateField()),
                ('extensionEndDate', models.DateField()),
                ('remarks', models.CharField(max_length=500)),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
