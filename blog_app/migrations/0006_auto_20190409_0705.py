# Generated by Django 2.1 on 2019-04-09 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_blog_categories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
