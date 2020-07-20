# Generated by Django 3.0.7 on 2020-06-17 19:41

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_random_street_wedding'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portrait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=100, size=[1200, 800], upload_to='images/portrait/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Random',
        ),
        migrations.AlterField(
            model_name='street',
            name='photo',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=100, size=[1200, 800], upload_to='images/street/'),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='photo',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=100, size=[1200, 800], upload_to='images/wedding/'),
        ),
    ]
