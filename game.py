from ctypes.wintypes import PINT
import random
def print_welcome():
  print('***************************************************************')
  print('************ WELCOME TO ROCK PAPER SCISSORS EAGLE ***************')
  print('***************************************************************')
  print()
  print("Welcome to RPSO: Rock, Paper, Scissors, EAGLE, a modified game of\nRock, Paper, and Scissors where you compete against Otus, SCSU’s\nEAGLE mascot. Press any key to get started. ")
  print("\nPress the RETURN key to get started")

  input()
  print()
def show_rules():
  print('Here are the rules of the game:')
  print()
  print('   *  All players start a round with 0 points. ')
  print('   *  A hand consists of both players (you and Otus) making a selection.')
  print('   *  The winner of each hand wins 2 points based on the following:')
  print("\t\U0001F989 Rock beats Scissors")
  print("\t\U0001F989 Scissors beats Paper")
  print("\t\U0001F989 Paper beats Rock")
  print("\t\U0001F989 EAGLE beats Paper & Scissors")
  print("   *  If you play an EAGLE and you lose (e.g. Otus plays a rock), you\nlose 3 points. If you win,you get 2 points.  ")
  print('   *  If you ever have less than 0 points you lose the round. ')
  print('   *  You can only play 2 EAGLEs per game ')
  print('   *  If you win 3 hands in a row in a round, you earn an extra EAGLE.  ')
  show_menu()

def show_score(TheUS_score, player_score, TheUS_EAGLE_count, player_EAGLE_count, game_number):
  print(f'SCORECARD: {game_number} Games Played')
  print("----------------------------")
  print("| PLAYER | SCORE | EAGLES LEFT")
  print("----------------------------")

  print(f'| TheUS | {TheUS_score}  |  {TheUS_EAGLE_count}')
  print(f'| YOU  | {player_score}  | {player_EAGLE_count}')

def show_menu():
  print('User Menu:')
  print()
  print('\t1. Show rules')
  print('\t2. Play game')
  print('\t3. Exit game')
  print()
  your_choice = int(input('Enter your choice:'))
  print()
  if your_choice == 1:
    show_rules()
  elif your_choice == 2:
    main()
  else:
    print()
    print('THANKS GOODBYE!!!')
    input('Press RETURN to go back')


def get_Octus_pick(TheUS_EAGLE_count):
  rand = random.randint(1,4)
  hand = ''
  if rand == 1:
    hand = 'ROCK'
  elif rand == 2:
    hand = 'PAPER'
  elif rand == 3:
    hand ='SCISSORS'
  elif rand == 4:
    hand ='EAGLE'

  if(TheUS_EAGLE_count==0 and hand=="EAGLE"):
      print("You have used all your EAGLE, chose something else!")
      get_Octus_pick(TheUS_EAGLE_count)

  return hand

def get_my_pick(play_EAGLE_count):
  pick =input("Make your choice: (ROCK, PAPER, SCISSORS, EAGLE): ").upper()

  if pick == "ROCK":
    hand = 'ROCK'
  elif pick == "PAPER":
    hand = 'PAPER'
  elif pick == "SCISSORS":
    hand ='SCISSORS'
  elif pick == "EAGLE":
    hand ='EAGLE'

  if(play_EAGLE_count==0 and pick=="EAGLE"):
      print("You have used all your EAGLE, chose something else!")
      get_my_pick(play_EAGLE_count)
  else:
   return hand

def main():
  TheUS_score = 0
  player_score = 0
  TheUS_EAGLE_count = 1
  play_EAGLE_count = 1
  game_number =0

  for game in range (1,4):
      game_number +=1
      player = get_my_pick(play_EAGLE_count)
      TheUS = get_Octus_pick(TheUS_EAGLE_count)

      if player == TheUS:
        print(f'You chose: {player}')
        print(f'TheUS chose: {TheUS}')

      elif player == "ROCK":
        if TheUS == "SCISSORS":
            print("Rock smashes scissors! You win!")
            player_score+=2
        elif TheUS == "EAGLE":
            print("Rock smashes an EAGLE! You win!")
            player_score+=2
            TheUS_EAGLE_count=0
            TheUS_score-=2
        else:
            print("Paper covers Rock! You lose.")
            TheUS_score+=2

      elif player == "PAPER":
        if TheUS == "ROCK":
            player_score+=2
            print("Paper covers rock! You win!")
        elif TheUS == "EAGLE":
            TheUS_EAGLE_count=0
            TheUS_score +=3
            print("EAGLE tear Paper! You lose!")

        else:
            TheUS_score+=2
            print("Scissors cuts paper! You lose.")


      elif player == "SCISSORS":
        if TheUS == "PAPER":
            player_score+=2
            print("Scissors cuts paper! You win!")

        elif TheUS == "EAGLE":
            TheUS_EAGLE_count=0
            TheUS_score+=3
            print("EAGLE break Scissors! You lose!")
        else:
            TheUS_score+=2
            print("Rock smashes scissors! You lose.")

      elif player == "EAGLE":
        play_EAGLE_count=0
        if TheUS == "PAPER":
            player_score+=3
            print("EAGLE tear paper! You win!")

        elif TheUS == "ROCK":
            print("ROCK break EAGLE! You lose!")
            TheUS_score+=2
            player_score-=2
        else:
            player_score+=3
            print("EAGLE break scissors! You win.")
      print()
      show_score(TheUS_score, player_score,TheUS_EAGLE_count, play_EAGLE_count,game_number)

  print()

  if(player_score>TheUS_score):
      print("YU WIN "+str(player_score)+" AGAINST TheUS: " +str(TheUS_score) )
  else:
      print("TheUS WINS: "+str(TheUS_score)+" AGAINST YOU: "+str(player_score))
  show_menu()
print_welcome()
show_menu()
