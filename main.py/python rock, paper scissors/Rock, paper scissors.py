import random
import time
import pygame


pygame.init()

win_sound = pygame.mixer.Sound("mixkit-fantasy-game-success-notification-270.wav")
lose_sound = pygame.mixer.Sound("mixkit-lose-fairy-shine-2022.wav")
tie_sound = pygame.mixer.Sound("mixkit-cowbell-sharp-hit-1743.wav")
game_over = pygame.mixer.Sound("mixkit-arcade-game-over-3068.wav")

options = ("rock", "paper", "scissors")
player_score = 0
computer_score = 0
current_round = 1
rounds_to_play = 5

# Welcome message
print("Welcome to the quest! In this game, you will face 5 rounds.")
print()
print("In each round, you will face an enemy, and your mission is to defeat them using the game of Rock, Paper, Scissors.")
print()
print("Earn a point for each victory. To successfully complete the quest, you must score at least 3 points out of the 5 rounds.")
print()
input("Press 'Enter' to start: ")


def Display_Score():
    print(f"Player Score: {player_score}")
    print(f"Computer Score: {computer_score}")

def continue_story():
    enemies = ["Boar", "Bear", "Dragon", "Witch"]
    enemy = random.choice(enemies)
    print(f"You encounter a {enemy}!, Defeat him!")
    return enemy


playing = True
while playing and current_round <= rounds_to_play:
    player = ''
    computer = random.choice(options)

    enemy = continue_story()
    print(f"-------Round {current_round}-------")
    player = input("Enter a choice, rock, paper, or scissors: ")

    if player not in options:
        print("Please enter 'rock', 'paper', or 'scissors'")
        continue

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
        tie_sound.play()
    elif (
        (player == "paper" and computer == "rock") or
        (player == "rock" and computer == "scissors") or
        (player == "scissors" and computer == "paper")
    ):
        print(f"You beat the {enemy}!")
        win_sound.play()
        player_score += 1
    else:
        print(f"You were defeated by the {enemy}!")
        lose_sound.play()
        computer_score += 1

    current_round += 1
    Display_Score()

    if player_score >=3:
        print("You have won the quest! Congratulations!")
    elif computer_score >=3:
        print("You got defeated! Try again!")
        game_over.play()

    if current_round <= rounds_to_play:
        play_again = input("Move on to the next round? (y/n)\n").lower()
        if play_again != 'y':
            Display_Score()
            break
    

print("Thank you for playing!:)")

