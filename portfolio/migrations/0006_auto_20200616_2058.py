# Generated by Django 3.0.7 on 2020-06-16 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20200616_1238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='review_body',
            new_name='message_body',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='review_body',
            new_name='message_body',
        ),
    ]
