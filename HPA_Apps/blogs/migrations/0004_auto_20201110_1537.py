# Generated by Django 3.0.3 on 2020-11-10 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20201110_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250, null=True, unique_for_date='publish'),
        ),
    ]
