# barbarian.py

import random

class Barbarian:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.proficiency_bonus = 2  # Default proficiency bonus
        self.hit_points = 12 + self.constitution_modifier()  # Level 1 HP (d12 + Con modifier)
        
        # Starting attributes
        self.strength = 16  # Primary ability score (Strength)
        self.dexterity = 14
        self.constitution = 14
        
        # Armor and AC
        self.armor_class = 13  # Base armor class (could be modified by armor)
        
        # Attack and damage modifiers
        self.attack_bonus = self.strength // 2  # Example: Strength modifier for attack rolls
        
        # Barbarian Features (Level 1)
        self.raging = False  # Whether the Barbarian is currently in a rage
        self.rage_damage_bonus = 2  # +2 damage while raging at level 1
        self.rages_left = 2  # 2 rages per day at level 1
        self.weapon_masteries = []  # Weapon mastery starts empty
        
        # Proficient saving throws
        self.proficient_saving_throws = ['Strength', 'Constitution']
        self.proficient_skills = []  # To be chosen by the player
        
        # Starting Equipment
        self.equipment = []  # Will be populated with chosen starting equipment
        
        # Level 1 Features
        self.features = {
            1: ['Rage', 'Unarmored Defense', 'Weapon Mastery'],
            2: ['Danger Sense', 'Reckless Attack'],
            3: ['Barbarian Subclass', 'Primal Knowledge'],
            4: ['Ability Score Improvement'],
            5: ['Extra Attack', 'Fast Movement'],
            6: ['Subclass feature'],
            7: ['Feral Instinct', 'Instinctive Pounce'],
            8: ['Ability Score Improvement'],
            9: ['Brutal Strike'],
            10: ['Subclass feature'],
            11: ['Relentless Rage'],
            12: ['Ability Score Improvement'],
            13: ['Improved Brutal Strike'],
            14: ['Subclass feature'],
            15: ['Persistent Rage'],
            16: ['Ability Score Improvement'],
            17: ['Improved Brutal Strike'],
            18: ['Indomitable Might'],
            19: ['Epic Boon'],
            20: ['Primal Champion']
        }

    def constitution_modifier(self):
        """Calculate the Constitution modifier."""
        return (self.constitution - 10) // 2

    def calculate_armor_class(self):
        """Calculate AC based on whether the Barbarian is wearing armor."""
        if self.armor_class == 13:  # If not wearing armor, use Unarmored Defense
            self.armor_class = 10 + (self.dexterity // 2) + (self.constitution // 2)  # Unarmored Defense
        return self.armor_class
    
    def rage(self):
        """Activate the Barbarian's rage."""
        if self.rages_left > 0 and not self.raging:
            self.raging = True
            self.rages_left -= 1
            print(f"{self.name} enters a rage! Damage is increased by {self.rage_damage_bonus}, and they gain resistance to certain damage types.")
        elif self.rages_left <= 0:
            print(f"{self.name} is out of rages for the day.")
        else:
            print(f"{self.name} is already in a rage!")

    def end_rage(self):
        """End the Barbarian's rage."""
        if self.raging:
            self.raging = False
            print(f"{self.name}'s rage ends.")
        else:
            print(f"{self.name} is not currently raging.")

    def attack(self):
        """Perform a melee attack. Account for strength, rage, and critical hits."""
        base_attack_roll = random.randint(1, 20)  # Simulate attack roll with d20
        if base_attack_roll == 20:  # Critical hit
            damage = self.strength + (self.level * 2)  # Example of crit bonus damage
            print(f"{self.name} lands a critical hit for {damage} damage!")
        else:
            damage = self.strength + self.attack_bonus
            if self.raging:
                damage += self.rage_damage_bonus  # Add rage bonus damage
                print(f"{self.name} attacks with rage, dealing {damage} damage!")
            else:
                print(f"{self.name} attacks, dealing {damage} damage.")

    def reckless_attack(self):
        """Activate Reckless Attack for advantage on melee attack rolls."""
        print(f"{self.name} uses Reckless Attack! They gain advantage on attack rolls but enemies gain advantage on attacks against them.")

    def danger_sense(self):
        """Activate Danger Sense. Grants advantage on Dexterity saving throws against visible effects."""
        print(f"{self.name} uses Danger Sense to avoid danger more effectively.")

    def level_up(self):
        """Level up the Barbarian. Add hit points and potentially improve abilities."""
        self.level += 1
        # Calculate new hit points with d12 + Constitution modifier
        new_hp = random.randint(1, 12) + self.constitution_modifier()
        self.hit_points += new_hp
        print(f"{self.name} levels up to level {self.level}! Gained {new_hp} HP. New HP: {self.hit_points}")
        
        # Apply class features at the new level
        if self.level in self.features:
            for feature in self.features[self.level]:
                print(f"{self.name} gains feature: {feature}")

    def choose_skills(self, skills):
        """Choose 2 skill proficiencies."""
        if len(skills) == 2:
            self.proficient_skills.extend(skills)
            print(f"{self.name} has chosen the following skills: {', '.join(skills)}")
        else:
            print("You must choose 2 skills.")

    def choose_equipment(self, choice):
        """Choose starting equipment (A or B)."""
        if choice == 'A':
            self.equipment = ['Greataxe', '4 Handaxes', 'Explorer\'s Pack', '15 GP']
            print(f"{self.name} has chosen Equipment A: Greataxe, 4 Handaxes, Explorer's Pack, and 15 GP.")
        elif choice == 'B':
            self.equipment = ['75 GP']
            print(f"{self.name} has chosen Equipment B: 75 GP.")
        else:
            print("Invalid choice. Choose either 'A' or 'B'.")
    
    def choose_weapon_masteries(self, weapons):
        """Choose 2 weapon masteries."""
        if len(weapons) == 2:
            self.weapon_masteries.extend(weapons)
            print(f"{self.name} has chosen the following weapon masteries: {', '.join(weapons)}")
        else:
            print("You must choose 2 weapons to master.")

# Example usage:
barb = Barbarian("Thorne", level=1)
barb.choose_skills(["Athletics", "Survival"])
barb.choose_equipment("A")
barb.choose_weapon_masteries(["Greataxe", "Handaxe"])
barb.rage()
barb.attack()
barb.end_rage()
barb.level_up()  # Level up to level 2 and get new features!
