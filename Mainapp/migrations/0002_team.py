# Generated by Django 4.2.7 on 2023-12-03 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('img', models.ImageField(upload_to='')),
                ('designation', models.CharField(max_length=20)),
            ],
        ),
    ]
