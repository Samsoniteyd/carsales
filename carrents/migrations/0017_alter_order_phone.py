# Generated by Django 4.2 on 2023-07-10 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrents', '0016_alter_slide_sub_title_alter_slide_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(default=0, null=True),
        ),
    ]