# Generated by Django 4.2.3 on 2023-07-22 14:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soccer_league_app', '0007_soccermatch_date'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='soccermatch',
            name='unique_soccer_match',
        ),
        migrations.RemoveField(
            model_name='soccermatch',
            name='guess_club',
        ),
        migrations.RemoveField(
            model_name='soccermatch',
            name='guess_goal',
        ),
        migrations.RemoveField(
            model_name='soccermatch',
            name='home_goal',
        ),
        migrations.AddField(
            model_name='soccermatch',
            name='away_club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='away_club', to='soccer_league_app.club'),
        ),
        migrations.AddField(
            model_name='soccermatch',
            name='ft_away_goal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='soccermatch',
            name='ft_home_goal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='soccermatch',
            name='ht_away_goal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='soccermatch',
            name='ht_home_goal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='soccermatch',
            name='time',
            field=models.TimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='soccermatch',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AddConstraint(
            model_name='soccermatch',
            constraint=models.UniqueConstraint(fields=('round', 'home_club', 'away_club'), name='unique_soccer_match'),
        ),
    ]
