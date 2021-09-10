# Generated by Django 3.2.5 on 2021-09-10 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='pay_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='payment',
            unique_together={('roll', 'registration_number', 'department', 'semester')},
        ),
    ]
