# Generated by Django 3.2 on 2021-04-25 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='others',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='remdisivr',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='specify_other',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='toclizumab',
            field=models.BooleanField(default=False),
        ),
    ]