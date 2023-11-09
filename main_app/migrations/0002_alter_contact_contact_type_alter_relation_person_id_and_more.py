# Generated by Django 4.1.7 on 2023-11-07 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.contacttype'),
        ),
        migrations.AlterField(
            model_name='relation',
            name='person_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.person'),
        ),
        migrations.AlterField(
            model_name='relation',
            name='relation_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.relationtype'),
        ),
    ]