# Generated by Django 4.2.3 on 2023-07-22 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccer_league_app', '0008_remove_soccermatch_unique_soccer_match_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='soccermatch',
            name='ft_result',
            field=models.TextField(default='D'),
        ),
        migrations.AddField(
            model_name='soccermatch',
            name='ht_result',
            field=models.TextField(default='D'),
        ),
    ]