# Generated by Django 4.2.1 on 2023-06-15 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0007_alter_product_total_reserved'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('start_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('description', models.TextField()),
                ('start_at', models.DateTimeField(auto_now=True)),
                ('end_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.DecimalField(decimal_places=2, max_digits=9)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.lot')),
            ],
        ),
        migrations.AddField(
            model_name='lot',
            name='final_rate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='final_lot', to='products.rate'),
        ),
        migrations.AddField(
            model_name='lot',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
