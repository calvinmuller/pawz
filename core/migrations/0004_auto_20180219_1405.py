# Generated by Django 2.0.2 on 2018-02-19 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180219_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paw',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Organisation'),
        ),
    ]