# Generated by Django 4.0.2 on 2022-07-30 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_pic', models.ImageField(upload_to='cover')),
                ('name', models.CharField(max_length=120)),
                ('dateofrelease', models.DateField(null=True)),
            ],
        ),
    ]
