# Generated by Django 3.1 on 2020-08-18 12:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('deutschstered', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-category_pub_date'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='item',
            name='item_draft_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 18, 12, 0, 42, 217842, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_pub_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_updated_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]