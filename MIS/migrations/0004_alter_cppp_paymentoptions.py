# Generated by Django 5.0.6 on 2024-07-09 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MIS', '0003_alter_cppp_emdtype_alter_cppp_l1bidderbg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cppp',
            name='paymentOptions',
            field=models.CharField(choices=[('10%', '10%'), ('25%', '25%'), ('50%', '50%'), ('75%', '75%'), ('90%', '90%'), ('100%', '100%')], max_length=50),
        ),
    ]
