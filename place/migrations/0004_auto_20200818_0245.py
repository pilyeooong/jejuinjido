# Generated by Django 3.0.3 on 2020-08-18 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0003_auto_20200818_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(null=True, upload_to='place/'),
        ),
        migrations.AlterField(
            model_name='place',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='website',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
