# Generated by Django 3.2.3 on 2021-05-25 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0023_merge_0016_auto_20210522_0424_0022_auto_20210522_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badword',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='subscribtion',
            name='subscribed_on',
            field=models.DateField(auto_now=True),
        ),
    ]
