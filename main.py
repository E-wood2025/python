print("Welcome to the D&D Character Creator!")

# Step 1: Ask for character name
character_name = input("What is your character's name? ")

# Step 2: Choose a species and show detailed traits
species_traits = {
    "Aasimar": {
        "Celestial Resistance": "Resistance to necrotic and radiant damage.",
        "Darkvision": "See in dim light within 60 feet as if it were bright light.",
        "Healing Hands": "Once per long rest, heal a creature equal to the number rolled on a number of d4s equal to your Proficiency Bonus.",
        "Light Bearer": "You know the Light cantrip.",
        "Celestial Revelation": "Gain temporary flight, an aura that damages foes, or radiate light (choose the option each time you transform)."
    },
    "Dragonborn": {
        "Dragon Ancestry": "Choose a dragon type that affects your breath weapon and resistance.",
        "Breath Weapon": "Use an action to exhale destructive energy (damage type based on ancestry).",
        "Damage Resistance": "Gain resistance to the damage type associated with your dragon ancestry.",
        "Darkvision": "See in dim light within 60 feet as if it were bright light.",
        "Draconic Flight": "Gain temporary wings at higher levels."
    },
    "Dwarf": {
        "Darkvision": "See in dim light within 120 feet as if it were bright light.",
        "Dwarven Resilience": "Advantage on saving throws against poison and resistance to poison damage.",
        "Dwarven Toughness": "Your hit point maximum increases by 1 for each level.",
        "Stonecunning": "Gain Tremorsense with a range of 60 feet for 10 minutes."
    },
    "Elf": {
        "Darkvision": "See in dim light within 60 feet as if it were bright light.",
        "Elven Lineage": "Choose a lineage that grants additional magic or weapon proficiencies.",
        "Fey Ancestry": "Advantage on saving throws against being charmed.",
        "Keen Senses": "You have proficiency in Insight, Perception, or Survival skill.",
        "Trance": "Elves don't sleep; instead, they meditate for 4 hours."
    },
    "Gnome": {
        "Darkvision": "See in dim light within 60 feet as if it were bright light.",
        "Gnomish Cunning": "Advantage on Intelligence, Wisdom, and Charisma saving throws.",
        "Gnomish Lineage": "Grants additional magical abilities determined by lineage, Forest or Rock."
    },
    "Goliath": {
        "Giant Ancestry": "Choose an elemental trait tied to your giant heritage; Cloud, Fire, Frost, Hill, Stone, or Storm.",
        "Large Form": "At character level 5, grow in size temporarily, increasing reach and carrying capacity.",
        "Powerful Build": "You have advantage on any ability check you make to end the Grappled condition. You count as one size larger for carrying and lifting."
    },
    "Halfling": {
        "Brave": "Advantage on saving throws against being frightened.",
        "Halfling Nimbleness": "You can move through the space of any creature larger than you.",
        "Luck": "Reroll a natural 1 on the d20 of any D20 test, you must use the new roll.",
        "Naturally Stealthy": "You can attempt to hide when you are obscured only by a creature that is at least one size larger than you."
    },
    "Human": {
        "Resourceful": "You gain Heroic Inspiration at the end of a long rest.",
        "Skillful": "Gain proficiency in one skill of your choice.",
        "Versatile": "Gain a feat of your choice."
    },
    "Orc": {
        "Adrenaline Rush": "Dash as a bonus action and gain temporary hit points.",
        "Darkvision": "See in dim light within 120 feet as if it were bright light.",
        "Relentless Endurance": "Drop to 1 HP instead of 0 once per long rest."
    },
    "Tiefling": {
        "Darkvision": "See in dim light within 60 feet as if it were bright light.",
        "Fiendish Legacy": "Gain innate spellcasting based on your infernal heritage.",
        "Otherworldly Presence": "You know the Thaumaturgy cantrip."
    }
}

# Subspecies, heritages, and legacies
subspecies_options = {
    "Dragonborn": ["Black (Acid)", "Blue (Lightning)", "Brass (Fire)", "Bronze (Lightning)", "Copper (Acid)", 
                   "Gold (Fire)", "Green (Poison)", "Red (Fire)", "Silver (Cold)", "White (Cold)"],
    "Elf": ["Drow", "High Elf", "Wood Elf"],
    "Gnome": ["Forest Gnome", "Rock Gnome"],
    "Goliath": ["Cloud's Jaunt (Cloud Giant)", "Fire's Burn (Fire Giant)", "Frost's Chill (Frost Giant)", 
                "Hill's Tumble (Hill Giant)", "Stone's Endurance (Stone Giant)", "Storm's Thunder (Storm Giant)"],
    "Tiefling": ["Abyssal", "Chthonic", "Infernal"]
}

# Display species choices
print("\nChoose your species:")
species_list = list(species_traits.keys())
for i, sp in enumerate(species_list, 1):
    print(f"{i}. {sp}")

# Get user input and validate it
while True:
    try:
        species_choice = int(input("\nEnter the number of your species: "))
        if 1 <= species_choice <= len(species_list):
            character_species = species_list[species_choice - 1]
            break
        else:
            print("Invalid choice. Please enter a number from the list.")
    except ValueError:
        print("Please enter a valid number.")

# Show detailed species traits
print(f"\nYour character, {character_name}, is a {character_species}.")
print("Traits:")
for trait, description in species_traits[character_species].items():
    print(f"  - {trait}: {description}")

# Ask for subspecies, heritage, or legacy if applicable
if character_species in subspecies_options:
    print("\nChoose your specific ancestry or heritage:")
    for i, option in enumerate(subspecies_options[character_species], 1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = int(input("\nEnter the number of your choice: "))
            if 1 <= choice <= len(subspecies_options[character_species]):
                specific_option = subspecies_options[character_species][choice - 1]
                break
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Please enter a valid number.")

    print(f"\nYour specific ancestry or heritage is: {specific_option}")

# Step 3: Ability Score Allocation
print("\nDistribute your ability scores (Standard Array: 15, 14, 13, 12, 10, 8):")
ability_scores = {
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0
}
for stat in ability_scores:
    while True:
        try:
            score = int(input(f"Enter value for {stat}: "))
            if score in [15, 14, 13, 12, 10, 8]:
                ability_scores[stat] = score
                break
            else:
                print("Invalid score. Please enter a valid value from the standard array.")
        except ValueError:
            print("Please enter a valid number.")

# Step 4: Class selection
print("\nChoose your class:")
classes = {
    "Barbarian": {
        "Rage": "You enter a primal power called Rage, a force that grants you extraordinary might and resilience.",
        "Unarmored Defense": "While not wearing any armor, your base Armor Class equals 10 plus your Dexterity and Constitution modifiers."
    },
    "Bard": {
        "Spellcasting": "You have learned to cast spells through your bardic arts.",
        "Bardic Inspiration": "You can supernaturally inspire others through words, music, or dance."
    },
    "Cleric": {
        "Spellcasting":"You have learned to cast spells through prayer and meditation.",
        "Divine Order": "You have dedicated yourself to one of the sacred roles, Protector or Thaumaturge."
    },
    "Druid": {
        "Spellcasting":"You have learned to cast spells through studying the mystical forces of nature.",
        "Primal Order":"You have dedicated yourself to one of the sacred orders, Magician or Warden."
    },
    "Fighter": {
        "Fighting Style":"You have honed your martial prowess and gain a Fighting Style feat of your choice.",
        "Second Wind":"You have a limited well of physical and mental stamina that you can draw on to regain Hit Points."
    },
    "Monk": {
        "Martial Arts":"Your practice of martial arts gives you mastery of combat styles that use your Unarmed Strike and Monk weapons.",
        "Unarmored Defense":"While you aren't wearing armor or wielding a Shield, your base Armor Class equals 10 plus your Dexterity and Wisdom modifiers."
    },
    "Paladin": {
        "Lay on Hands":"Your bless touch can heal wounds.",
        "Spellcasting":"You have learned to cast spells through prayer and meditation."
    },
    "Ranger": {
        "Spellcasting":"You have learned to channel the magical essence of nature to cast spells.",
        "Favored Enemy":"You always have the Hunter's Mark spell prepared. You can cast it twice without expending a spell slot."
    },
    "Rogue": {
        "Expertise":"You gain Expertise in two of your skill proficiencies of your choice. At level 6, you gain Expertise in two more skill proficiencies.",
        "Sneak Attack":"You know how to strike subtly and exploit a foe's distraction. Once per turn, you can deal extra damage to a creature you hit with a Finesse or ranged weapon."
    },
    "Sorcerer": {
        "Spellcasting":"Drawing from your innate magic, you can cast spells.",
        "Innate Sorcery":"An event in your past left an indelible mark on you, infusing you with simmering magic. Unleashing this magic, increases your the DC of your Sorcerer spells and you have Advantage on attack rolls with Sorcerer spells you cast."
    },
    "Warlock": {
        "Eldritch Invocations":"You have unearthed Eldritch Invocations, pieces of forbidden knowledge that imbue you win an abiding magical abilty or other lessons.",
        "Pact Magic":"Through occult ceremony, you have forrmed a pact with a mysterious entity to gain magical powers."
    },
    "Wizard": {
        "Spellcasting":"As a student of arcane magic, you have learned to cast spells.",
        "Arcane Recovery": "You can regain some of your magical energy by using your spellbook."
    },    
}
class_list = list(classes.keys())
for i, cl in enumerate(class_list, 1):
    print(f"{i}. {cl}")

# Get user input for class choice
while True:
    try:
        class_choice = int(input("\nEnter the number of your class: "))
        if 1 <= class_choice <= len(class_list):
            character_class = class_list[class_choice - 1]
            break
        else:
            print("Invalid choice. Please enter a number from the list.")
    except ValueError:
        print("Please enter a valid number.")

print(f"\nYour character, {character_name}, is a {character_class}.")
print("Class Features:")
for feature, description in classes[character_class].items():
    print(f"  - {feature}: {description}")

# Step 5: Background selection
backgrounds = {
   "Acolyte": {"Ability Scores: Intelligence, Wisdom, Charisma","Feat: Magic Initiate (Cleric)","Skill Proficiencies: Insight and Religion","Tool Proficiency: Calligrapher's Supplies."},
    "Artisan": {"Ability Scores: Strength, Dexterity, Intelligence","Feat: Crafter","Skill Proficiencies: Investigation and Persuasion","Tool Proficiency: Choose one kind of Artisan's Tools."},
    "Charlatan": {"Ability Scores: Dexterity, Constitution, Charisma","Feat: Skilled","Skill Proficiencies: Deception and Sleight of Hand","Tool Proficiency: Forgery Kit."},
    "Criminal": {"Ability Scores: Dexterity, Constitution, Intelligence","Feat: Alert","Skill Proficiencies: Sleight of Hand and Stealth","Tool Proficiency: Thieves' Tools."},
    "Entertainer": {"Ability Scores: Strength, Dexterity, Charisma","Feat: Musician","Skill Proficiencies: Acrobatics and Performance","Tool Proficiency: Choose one kind of Musical Instrument."},
    "Farmer": {"Ability Scores: Strength, Constitution, Wisdom","Feat: Tough","Skill Proficiencies: Animal Handling and Nature","Tool Proficiency: Carpenter's Tools."},
    "Guard": {"Ability Scores: Strength, Intelligence, Wisdom","Feat: Alert","Skill Proficiencies: Athletics and Perception","Tool Proficiency: Choose one kind of Gaming Set."},
    "Guide": {"Ability Scores: Dexterity, Constitution, Wisdom","Feat: Magic Initiate (Druid)","Skill Proficiencies: Stealth and Survival","Tool Proficiency: Cartographer's Tools."},
    "Hermit": {"Ability Scores: Constitution, Wisdom, Charisma","Feat: Healer","Skill Proficiencies: Medicine and Religion","Tool Proficiency: Herbalism Kit."},
    "Merchant": {"Ability Scores: Constitution, Intelligence, Charisma","Feat: Lucky","Skill Proficiencies: Animal Handling and Persuasion","Tool Proficiency: Navigator's Tools."},
    "Noble": {"Ability Scores: Strength, Intelligence, Charisma","Feat: Skilled","Skill Proficiencies: History and Persuasion","Tool Proficiency: Choose one kind of Gaming Set."},
    "Sage": {"Ability Scores: Constitution, Intelligence, Wisdom","Feat: Magic Initiate (Wizard)","Skill Proficiencies: Arcana and History","Tool Proficiency: Calligrapher's Supplies."},
    "Sailor": {"Ability Scores: Strength, Dexterity, Wisdom","Feat: Tavern Brawler","Skill Proficiencies: Acrobatics and Perception","Tool Proficiency: Navigator's Tools."},
    "Scribe": {"Ability Scores: Dexterity, Intelligence, Wisdom","Feat: Skilled","Skill Proficiencies: Investigation and Perception","Tool Proficiency: Calligrapher's Supplies."},
    "Soldier": {"Ability Scores: Strength, Dexterity, Constitution","Feat: Savage Attacker","Skill Proficiencies: Athletics and Intimidation","Tool Proficiency: Choose one kind of Gaming Set."}, 
    "Wayfarer":{"Ability Scores: Dexterity, Wisdom, Charisma","Feat: Lucky","Skill Proficiencies: Insight and Stealth","Tool Proficiency: Thieves' Tools."},
}
background_list = list(backgrounds.keys())
for i, bg in enumerate(background_list, 1):
    print(f"{i}. {bg}")

# Get user input for background choice
while True:
    try:
        background_choice = int(input("\nEnter the number of your background: "))
        if 1 <= background_choice <= len(background_list):
            character_background = background_list[background_choice - 1]
            break
        else:
            print("Invalid choice. Please enter a number from the list.")
    except ValueError:
        print("Please enter a valid number.")

print(f"\nYour character, {character_name}, has the {character_background} background.")
print("Background Features:")
for feature, description in backgrounds[character_background].items():
    print(f"  - {feature}: {description}")

# Step 6: Alignment
alignments = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "True Neutral", "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil"]
print("\nChoose your alignment:")
for i, align in enumerate(alignments, 1):
    print(f"{i}. {align}")

while True:
    try:
        alignment_choice = int(input("\nEnter the number of your alignment: "))
        if 1 <= alignment_choice <= len(alignments):
            character_alignment = alignments[alignment_choice - 1]
            break
        else:
            print("Invalid choice. Please enter a number from the list.")
    except ValueError:
        print("Please enter a valid number.")

print(f"\nYour character's alignment is {character_alignment}.")

# Summary of the character
print("\nCharacter Summary:")
print(f"Name: {character_name}")
print(f"Species: {character_species}")
print(f"Class: {character_class}")
print(f"Background: {character_background}")
print(f"Alignment: {character_alignment}")
print("Ability Scores:")
for stat, score in ability_scores.items():
    print(f"  - {stat}: {score}")
