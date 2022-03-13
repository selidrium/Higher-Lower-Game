from game_data import data
from art import logo, vs
import random
from replit import clear


# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.

def get_random_account():
  """Get data from random account"""
  celeb = random.choice(data)
  return celeb

def format(account):
  """Format account into printable format: name, description and country"""
  name = account['name']
  description = account['description']
  country = account['country']
  return f"{name}, a {description}, from {country}"

def check_followers(guess, a_followers, b_followers):
  """Compare followers and return answer"""
  if a_followers > b_followers:
    return guess == 'a'
  else:
    return guess == 'b'

def game():
  play_again = True
  score = 0
  print(logo)
  while play_again == True:
    account_a = get_random_account()
    account_b = get_random_account()
    
    if account_a == account_b:
      account_b = get_random_account()
    
    
    print(f"Compare A: {format(account_a)}.")
    print(vs)
    print(f"Against B: {format(account_b)}.")
    
    
    print(account_a["follower_count"])
    print(account_b["follower_count"])
    
    user_guess = input("Press 'A' or 'B' to choose: ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_followers(user_guess, a_follower_count, b_follower_count)
    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      play_again = False
      print(f"Sorry, that's wrong. Final score: {score}")

    

game()