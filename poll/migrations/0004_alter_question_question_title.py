# Generated by Django 4.1 on 2023-12-12 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_alter_question_question_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
