# Generated by Django 2.0.5 on 2018-06-02 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_url', models.CharField(max_length=3000)),
                ('shortened_url', models.CharField(max_length=10)),
                ('count', models.PositiveIntegerField()),
            ],
        ),
    ]
