# Generated by Django 2.0.2 on 2018-02-19 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_paw_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paw',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paws', to='core.Organisation'),
        ),
    ]
