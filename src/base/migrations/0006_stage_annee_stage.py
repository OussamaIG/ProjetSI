# Generated by Django 4.0.1 on 2022-01-25 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_palier_code_stage'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='annee_stage',
            field=models.IntegerField(null=True),
        ),
    ]
