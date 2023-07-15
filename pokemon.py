class Pokemon:
  def __init__(self, name, level, poke_type, health, max_health, is_knocked_out, total_xp):
    self.name = name
    self.level = level
    self.poke_type = poke_type
    self.health = health
    self.max_health = max_health
    self.is_knocked_out = is_knocked_out
    self.total_xp = total_xp

  def lose_health(self, damage):
    self.health -= damage
    print(self.name + " just lost " + str(damage) + " health." + "\n")
    return

  def gain_health(self, heal_amount):
    self.health + heal_amount
    return print(self.name + " just healed " + str(heal_amount) + " health." + "\n")

  def knock_out(self):
    if self.health == 0:
      self.is_knocked_out = True
      return print(self.name + " is knocked out." + "\n")

  def revive(self):
    self.is_knocked_out = False
    return print(self.name + " is awake." + "\n")

  def attack(self, other):
    damage = 0
    if self.is_knocked_out == True:
      knocked_out_message = self.name + " is knocked out and can't attack." + "\n"
      print(knocked_out_message)
      return None
    elif self.is_knocked_out == False:
      if self.poke_type == "Fire" and other.poke_type == "Grass":
        damage = other.level * 2
      if self.poke_type == "Fire" and other.poke_type == "Water":
        damage = other.level / 2
      if self.poke_type == "Fire" and other.poke_type == "Fire":
        damage = other.level 
      if self.poke_type == "Grass" and other.poke_type == "Water":
        damage = other.level * 2
      if self.poke_type == "Grass" and other.poke_type == "Fire":
        damage = other.level / 2
      if self.poke_type == "Grass" and other.poke_type == "Grass":
        damage = other.level 
      if self.poke_type == "Water" and other.poke_type == "Grass":
        damage = other.level / 2
      if self.poke_type == "Water" and other.poke_type == "Fire":
        damage = other.level * 2
      if self.poke_type == "Water" and other.poke_type == "Water":
        damage = other.level 
      print(self.name + " attacks with a " + self.poke_type.lower() + " attack!!" + "\n")
      self.gain_xp(other.level * 25)
      return other.lose_health(damage)

  def gain_xp(self, xp_amount):
    self.total_xp += xp_amount
    print(self.name + " just gained " + str(xp_amount) + " XP!" + "\n" + self.name + " now has " + str(self.total_xp) + " XP!" + "\n")
    if self.total_xp > (self.level * 55):
      return self.evolve()
    else:
      return None

  def evolve(self):
    self.level += self.level
    print(self.name + " has evolved!" + "\n" + self.name + " is now level " + str(self.level) )
    return None

class Trainer:
  def __init__(self, name, potions, active_pokemon, pokemons):
    self.name = name
    self.potions = potions
    self.active_pokemon = active_pokemon
    self.pokemons = pokemons

  def use_potion(self): 
    heal_amount = 10
    heal_threshold = 91
    if self.active_pokemon.health > heal_threshold and self.active_pokemon.health < self.active_pokemon.max_health:
      #print(self.name + " just used a potion on " + self.active_pokemon.name)
      self.active_pokemon.gain_health(heal_amount)
      print("The amount healed was too much. " + self.active_pokemon.name + "\'s health was set to " + str(self.active_pokemon.max_health + "\n"))
      self.active_pokemon.health = self.active_pokemon.max_health
      return  
    else:
      #print(self.name + " just used a potion on " + self.active_pokemon.name)
      return self.active_pokemon.gain_health(heal_amount)

  def attack_other_trainer(self, other_trainer):
    their_pokemon=other_trainer.active_pokemon
    return self.active_pokemon.attack(their_pokemon)

  def switch_pokemon(self, pokemon):
    if pokemon.is_knocked_out == True:
      knocked_out_message = pokemon.name + " is knocked out and can't attack."
      print(knocked_out_message)
      return None
    elif pokemon.is_knocked_out == False:
      self.active_pokemon = pokemon
      print(self.name + " just changed over to " + str(self.active_pokemon.name) + "!")
      return self.active_pokemon

class Charmander(Pokemon):
  pass

water_pokemon = Pokemon("Water Pokemon", 1, "Water", 100, 100, False, 0)
fire_pokemon = Pokemon("Fire Pokemon", 1, "Fire", 100, 100, False, 0)
grass_pokemon = Pokemon("Grass Pokemon", 1, "Grass", 100, 100, False, 0)
trainer_zero = Trainer("Zero", 3, water_pokemon, [water_pokemon, fire_pokemon, grass_pokemon])
trainer_duo = Trainer("Duo", 3, grass_pokemon,[fire_pokemon, water_pokemon, grass_pokemon])


print(trainer_zero.attack_other_trainer(trainer_duo))
print(trainer_zero.attack_other_trainer(trainer_duo))
print(trainer_zero.attack_other_trainer(trainer_duo))
trainer_zero.active_pokemon.level = 2
print(trainer_zero.active_pokemon.level)
print(trainer_zero.active_pokemon.total_xp)



    