# Generated by Django 3.0.2 on 2020-01-24 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50)),
                ('Dishname', models.CharField(max_length=50)),
                ('Recipe', models.TextField()),
            ],
        ),
    ]