# Generated by Django 2.2.5 on 2019-09-15 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='Sith',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenofthesith.Planet')),
            ],
        ),
        migrations.CreateModel(
            name='Rookie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('age', models.PositiveSmallIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenofthesith.Planet')),
                ('sith', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ordenofthesith.Sith')),
            ],
        ),
        migrations.CreateModel(
            name='BlackHandTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ordenofthesith.Planet')),
                ('questions', models.ManyToManyField(to='ordenofthesith.Questions')),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.NullBooleanField()),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenofthesith.Questions')),
                ('rookie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenofthesith.Rookie')),
            ],
        ),
    ]
