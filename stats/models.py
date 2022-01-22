from django.db import models


VEHICLE_CLASS_CHOICES = [
    ('ground', (
        ('ground_light_tank', 'Light Tank'),
        ('ground_medium_tank', 'Medium Tank'),
        ('ground_heavy_tank', 'Heavy Tank'),
        ('ground_MBT', 'Main Battle Tank'),
        ('ground_SPAA', 'Self-propelled Anti Air'),
        ('ground_SPG', 'Self-propelled Gun'),
        ('ground_ATGM', 'Anti-Tank Guided Missile Carrier'),
        ('ground_SAM', 'Surface-to-Air Missile Carrier')
    )),
    ('aircraft_fixed_wing', (
        ('aircraft_fw_prop_fighter', 'Fighter (Propeller)'),
        ('aircraft_fw_jet_fighter', 'Fighter (Jet)'),
        ('aircraft_fw_prop_attacker', 'Attacker (Propeller)'),
        ('aircraft_fw_jet_attacker', 'Attacker (Jet)'),
        ('aircraft_fw_prop_bomber', 'Bomber (Propeller)'),
        ('aircraft_fw_jet_bomber', 'Bomber (Jet)')
    )),
    ('aircraft_rotary_wing', (
        ('aircraft_rw_attack', 'Attack Helicopter'),
        ('aircraft_rw_scout', 'Scout Helicopter'),
        ('aircraft_rw_utility', 'Utility Helicopter'),
    )),
    ('naval_bluewater', (
        ('naval_bw_destroyer', 'Destroyer'),
        ('naval_bw_light_cruiser', 'Light Cruiser'),
        ('naval_bw_heavy_cruiser', 'Heavy Cruiser'),
        ('naval_bw_battlecruiser', 'Battlecruiser'),
        ('naval_bw_battleship', 'Battleship'),
    )),
    ('naval_coastal', (
        ('naval_coastal_barge', 'Barge'),
        ('naval_coastal_ferry', 'Ferry'),
        ('naval_coastal_boat', 'Boat'),
        ('naval_coastal_sub_chaser', 'Sub-chaser'),
        ('naval_coastal_frigate', 'Frigate')
    ))
]


GAMEMODE_CHOICES = [
    ('Air', (
        ('air_arcade', 'Air Arcade Battle'),
        ('air_realistic', 'Air Realistic Battle'),
        ('air_realistic_ec', 'Air Realistic Enduring Confrontation Battle'),
        ('air_simulator', 'Air Simulator Battle'),
        ('air_simulator_ec', 'Air Simulator Enduring Confrontation Battle'),
    )),
    ('Helicopter', (
        ('heli_arcade', 'Helicopter Arcade Battle'),
        ('heli_arcade_ec', 'Helicopter Arcade Enduring Confrontation Battle'),
        ('heli_realistic', 'Helicopter Realistic Battle'),
        ('heli_realistic_ec', 'Helicopter Realistic Enduring Confrontation Battle'),
        ('heli_simulator', 'Helicopter Simulator Battle'),
        ('heli_simulator_ec', 'Helicopter Simulator Enduring Confrontation Battle'),
    )),
    ('Ground', (
        ('ground_arcade', 'Ground Arcade Battle'),
        ('ground_realistic', 'Ground Realistic Battle'),
        ('ground_simulator', 'Ground Simulator Battle'),
    )),
    ('Naval', (
        ('naval_arcade', 'Naval Arcade Battle'),
        ('naval_arcade_ec', 'Naval Arcade Enduring Confrontation Battle'),
        ('naval_realistic', 'Naval Realistic Battle'),
        ('naval_realistic_ec', 'Naval Realistic Enduring Confrontation Battle')
    ))
]


class Battle(models.Model):
    is_victory = models.BooleanField()
    with_premium = models.BooleanField()
    gamemode = models.CharField(max_length=30, choices=GAMEMODE_CHOICES)
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    zone_captures = models.IntegerField()
    damage_naval = models.IntegerField(blank=True, null=True)
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
