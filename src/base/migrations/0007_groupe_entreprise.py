# Generated by Django 4.0.1 on 2022-01-25 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_stage_annee_stage'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupe',
            name='entreprise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.entreprise'),
        ),
    ]
