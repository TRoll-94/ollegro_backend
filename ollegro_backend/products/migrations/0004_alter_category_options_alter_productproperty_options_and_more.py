# Generated by Django 4.2.1 on 2023-06-10 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_category_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='productproperty',
            options={'verbose_name': 'Product property', 'verbose_name_plural': 'Product properties'},
        ),
        migrations.AlterUniqueTogether(
            name='productproperty',
            unique_together={('code', 'category')},
        ),
    ]
