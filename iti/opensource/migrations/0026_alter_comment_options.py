# Generated by Django 3.2.3 on 2021-05-25 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0025_comment_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_added']},
        ),
    ]
