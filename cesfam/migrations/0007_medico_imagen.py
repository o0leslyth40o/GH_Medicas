# Generated by Django 4.0.5 on 2024-07-17 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cesfam', '0006_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='imagen',
            field=models.ImageField(null=True, upload_to='medico'),
        ),
    ]
