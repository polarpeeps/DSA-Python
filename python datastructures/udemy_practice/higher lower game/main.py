# from datafile import data,logo,vs
# import random,os
# s = True
# os.system("cls")
# def get_data(data):
#     ra = random.randint(0,len(data))
#     temp_dict = data[ra]
#     print(f"{temp_dict['name']}, a {temp_dict['description']}, from {temp_dict['country']}")
#     # print(f"{temp_dict}")
#     return temp_dict
# # def format_data(a):

# def compare_data(guess,a,b):
      
#       if  a['follower_count']>b['follower_count']:
#            print(f"{a['name']} has more followers ({a['follower_count']}M) than {b['name']} ({b['follower_count']}M)")
#            return guess =='a'
#       else:
#            print(f"{b['name']} has more followers ({b['follower_count']}M) than {a['name']} ({a['follower_count']}M)")
#            return guess == 'b'
#       return 0
# score =0 
# dat2 = get_data(data)
# game_cont = True
# print(logo)
# while game_cont:
#      # os.system("cls")
#      dat1 =  dat2
#      print(dat1)
#      print(vs)
#      dat2 = get_data(data)
#      while dat1==dat2:
#           print(vs)
#           dat2 = get_data(data)
#      guess = input("Guess who has more followers!! A or B :").lower()

#      check = compare_data(guess,dat1,dat2)
#      # score = 0
#      if check:
#           score += 1
#           print(f"THAT'S RIGHT, CURRENT SCORE: {score}")
     
#      else:
          
#           print(f"DANG THAT'S WRONG, SCORE: {score}")
#           game_cont = False


# from game_data import data
import random
from datafile import logo, vs,data
# from replit import clear
import os

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    os.system("cls")
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()