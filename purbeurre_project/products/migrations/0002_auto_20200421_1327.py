# Generated by Django 3.0.4 on 2020-04-21 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(editable=False, max_length=100, null=True, unique=True),
        ),
    ]