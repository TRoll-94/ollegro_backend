# Generated by Django 4.2.1 on 2023-05-28 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='users.usertype'),
        ),
    ]