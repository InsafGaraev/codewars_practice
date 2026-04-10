def combat(health, damage):
    The_players_updated_health = (health-damage)
    if health < damage:
         return The_players_updated_health == 0
    return The_players_updated_health