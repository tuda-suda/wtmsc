from django.db import models

from .model_choices import VEHICLE_CLASS_CHOICES, GAMEMODE_CHOICES


class Battle(models.Model):
    is_victory = models.BooleanField()
    with_premium = models.BooleanField(default=True)
    gamemode = models.CharField(max_length=30, choices=GAMEMODE_CHOICES)
    points = models.IntegerField()
    air_kills = models.IntegerField(default=0)
    ground_kills = models.IntegerField(default=0)
    naval_kills = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    zone_captures = models.IntegerField(default=0)
    base_bombing_TNT = models.DecimalField(decimal_places=2, default=0)
    bases_destroyed = models.IntegerField(default=0)
    sl_reward = models.IntegerField()
    rp_reward = models.IntegerField()
    activity = models.DecimalField(max_digits=3)
    in_game_time = models.TimeField()
    game_duration = models.TimeField()
    match_date = models.DateTimeField(auto_now_add=True)


class Vehicle(models.Model):
    name = models.SlugField(unique=True)
    display_name = models.TextField()
    sl_base_reward = models.DecimalField(max_digits=2, decimal_places=2)
    rp_base_reward = models.DecimalField(max_digits=2, decimal_places=2)
    tier = models.PositiveSmallIntegerField(min_value=1)
    BR = models.DecimalField(max_digits=2, decimal_places=1)
    class_ = models.CharField(max_legth=30, choices=VEHICLE_CLASS_CHOICES)
    is_premium = models.BooleanField()

    battles = models.ForeignKey(Battle, on_delete=models.RESTRICT, related_name='vehicles')
