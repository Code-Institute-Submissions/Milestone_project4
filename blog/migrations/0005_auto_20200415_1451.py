# Generated by Django 2.2 on 2020-04-15 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200414_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programmer',
            name='company',
        ),
        migrations.RemoveField(
            model_name='programmer',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
        migrations.DeleteModel(
            name='company',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='Programmer',
        ),
    ]