# Generated by Django 4.2.2 on 2023-07-07 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('im', models.ImageField(upload_to='pics')),
                ('na', models.CharField(max_length=150)),
                ('des', models.TextField()),
            ],
        ),
    ]
