# Generated by Django 5.0.6 on 2024-05-19 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_text', models.CharField(max_length=100)),
                ('due_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
