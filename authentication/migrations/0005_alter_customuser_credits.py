# Generated by Django 4.2.7 on 2024-01-02 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_customuser_options_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='credits',
            field=models.IntegerField(default=1),
        ),
    ]
