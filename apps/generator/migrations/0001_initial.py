# Generated by Django 4.0.4 on 2023-05-15 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password_text', models.CharField(max_length=255)),
                ('length', models.IntegerField()),
                ('uppercase', models.BooleanField()),
                ('lowercase', models.BooleanField()),
                ('numbers', models.BooleanField()),
                ('special_characters', models.BooleanField()),
            ],
        ),
    ]
