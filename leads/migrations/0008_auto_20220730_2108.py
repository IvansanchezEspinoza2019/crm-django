# Generated by Django 3.1.4 on 2022-07-30 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0007_category_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leads.userprofilemodel'),
        ),
    ]