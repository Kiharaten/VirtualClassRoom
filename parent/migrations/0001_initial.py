# Generated by Django 3.1.1 on 2021-02-03 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.IntegerField(default=0)),
                ('birthday', models.DateField(verbose_name='date birthday')),
            ],
        ),
    ]