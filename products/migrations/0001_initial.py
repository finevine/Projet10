# Generated by Django 3.0.7 on 2020-06-10 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=400, verbose_name='Category name')),
                ('slug', models.SlugField(editable=False, max_length=151, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Catégorie',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('code', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Nom')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('nutritionGrade', models.CharField(max_length=1, null=True, verbose_name='Nutriscore')),
                ('image', models.URLField(null=True)),
                ('fat', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Fat in 100g')),
                ('satFat', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Saturated fat in 100g')),
                ('sugar', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Sugar in 100g')),
                ('salt', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Salt in 100g')),
                ('category', models.ManyToManyField(related_name='category', to='products.Category', verbose_name='Catégorie')),
                ('compared_to_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='products.Category')),
            ],
            options={
                'verbose_name': 'Produit',
                'ordering': ['category__id'],
            },
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('healthy_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='healthy', to='products.Product')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('unhealthy_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unhealthy', to='products.Product')),
            ],
            options={
                'ordering': ['healthy_product'],
            },
        ),
        migrations.AddConstraint(
            model_name='favourite',
            constraint=models.UniqueConstraint(fields=('healthy_product', 'unhealthy_product'), name='unique_favourite'),
        ),
    ]