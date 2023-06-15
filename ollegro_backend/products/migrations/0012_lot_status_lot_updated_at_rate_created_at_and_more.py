# Generated by Django 4.2.1 on 2023-06-15 11:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_lot_sale_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot',
            name='status',
            field=models.CharField(choices=[('OPEN', 'Open'), ('PROCESS', 'Process'), ('CLOSED', 'Closed')], default='OPEN', max_length=12),
        ),
        migrations.AddField(
            model_name='lot',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='rate',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lot',
            name='start_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
