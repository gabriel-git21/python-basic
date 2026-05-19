#!/usr/bin/env python3
"""RPG Terraria boss fight like turn game.

A mini-game to test my Python skills and knowledge.

Author: ___JAO.DAS.JAPAS___
Version: 1.0
"""

# Beginning of the scene

player_health = 200
Boss_eye_health = 500

while player_health > 0 and Boss_eye_health > 0:

    print("You feel an evil presence watching you...")
    print("Choose your action")
    print("1. Attack")
    print("2. Defend")
    print("3. Roll")
    print("4. Potion")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        Boss_eye_health -= 50
        print("You attacked the eye! -50HP")

    elif choice == '2':
        player_health -= 20
        print("You defended yourself!")

    elif choice == '3':
        print("You escaped from the attack!")

    elif choice == '4':
        player_health += 15
        print("You drank a potion! +15HP")

    else:
        print("Invalid choice, go talk to Guide!")

    # Enemy attacks

    if Boss_eye_health > 0:
        player_health -= 15
        print("The enemy strikes back!")

if player_health <= 0:
    print("You were defeated by the enemy...")

elif Boss_eye_health <= 0:
    print("You defeated the enemy!")
