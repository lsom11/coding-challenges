def declare_winner(fighter1, fighter2, first_attacker):
    attacker = first_attacker
    while fighter1.health > 0 or fighter2.health > 0:
        if fighter1.name == attacker:
            fighter2.health -= fighter1.damage_per_attack
            attacker = fighter2.name
            if fighter2.health <= 0: return fighter1.name
        else:
            fighter1.health -= fighter2.damage_per_attack
            attacker = fighter1.name
            if fighter1.health <= 0: return fighter2.name
    
            
