# Generated by Django 3.1.7 on 2021-10-23 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('integers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={},
        ),
        migrations.RemoveField(
            model_name='person',
            name='hobbies',
        ),
        migrations.DeleteModel(
            name='Hobby',
        ),
    ]
