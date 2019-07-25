# Generated by Django 2.2.3 on 2019-07-24 05:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Common',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentId', models.IntegerField(unique=True)),
                ('sigungu', models.IntegerField()),
                ('area', models.IntegerField()),
                ('category', models.IntegerField()),
                ('title', models.TextField()),
                ('tel', models.TextField()),
                ('overview', models.TextField()),
                ('addr1', models.TextField()),
                ('addr2', models.TextField()),
                ('homepage', models.TextField()),
                ('avgScore', models.FloatField()),
                ('zipCode', models.IntegerField()),
                ('image', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.TextField()),
                ('endTime', models.TextField()),
                ('parking', models.TextField()),
                ('chkPet', models.TextField()),
                ('chkBaby', models.TextField()),
                ('restDate', models.TextField()),
                ('useTime', models.TextField()),
                ('ageLimit', models.TextField()),
                ('pay', models.TextField()),
                ('barbeque', models.TextField()),
                ('refund', models.TextField()),
                ('subevent', models.TextField()),
                ('openPeriod', models.TextField()),
                ('discountInfo', models.TextField()),
                ('chkCook', models.TextField()),
                ('openTime', models.TextField()),
                ('chkPack', models.TextField()),
                ('chkSmoking', models.TextField()),
                ('infoCenter', models.TextField()),
                ('detailId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.Common')),
            ],
        ),
        migrations.CreateModel(
            name='Stamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.Common')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'inform')},
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('inform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.Common')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'inform')},
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('inform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.Common')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'inform')},
            },
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.Common')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'inform')},
            },
        ),
    ]