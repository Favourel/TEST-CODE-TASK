# Generated by Django 4.0.4 on 2022-05-31 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_alter_reservation_checkin_alter_reservation_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.reservation'),
        ),
    ]
