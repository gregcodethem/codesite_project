# Generated by Django 2.0 on 2019-09-01 13:03

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_copywritingsettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copywritingsettings',
            name='hero_lead',
            field=wagtail.core.fields.RichTextField(help_text='Hero Lead Text', max_length=255),
        ),
    ]
