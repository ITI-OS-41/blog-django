# Generated by Django 3.0 on 2021-05-22 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0015_badword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badword',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='badword',
            name='word',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]