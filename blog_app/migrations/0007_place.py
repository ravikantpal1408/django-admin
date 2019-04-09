# Generated by Django 2.1 on 2019-04-09 07:40

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_auto_20190409_0705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', djgeojson.fields.PointField()),
            ],
        ),
    ]
