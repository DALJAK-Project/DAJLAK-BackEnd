# Generated by Django 2.2.5 on 2021-10-20 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('desc', models.TextField(max_length=300)),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=300)),
                ('image', models.ImageField(upload_to='')),
                ('thumnail_img', models.ImageField(upload_to='')),
                ('tag', models.CharField(max_length=40)),
                ('views', models.PositiveIntegerField(default=0, verbose_name='조회수')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
