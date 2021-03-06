# Generated by Django 3.2.10 on 2022-01-24 11:48

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('cart', '0002_wardrobe'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartlist',
            options={'ordering': ['date_added']},
        ),
        migrations.AddField(
            model_name='wardrobe',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterModelTable(
            name='cartlist',
            table='cartlist',
        ),
        migrations.AlterModelTable(
            name='wardrobe',
            table='wardrobe',
        ),
    ]
