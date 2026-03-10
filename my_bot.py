from secret import my_username
import random

"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  if "robot" in user_message:
    return True
  else:
    return False

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where theoriginal message was sent.
* You can have the bot respond differently to different messages and users
"""
dealer = 0
player = None
balance = 0
BJ_started = 0
number = 0
your_card = 0
dealer_card = 0
your_card2 = 0
your_card_total= 0
dealer_total_card = 0
game_started = False
game_running = False
# def            respond(user_message, user_name):
#   return f"""you said my name!!
#   {user_message.replace("robot", user_name)}"""
# cards =["1","2","3","4","5","6","7","8","9","jack","queen","king", "ace"]
card = [1, 2, 3, 4, 5 ,6 ,7, 8, 9, 10, 10, 10, 10]
def respond(user_message,user_name):
  global card
  global player
  global dealer
  global balance
  global BJ_started
  global number
  global your_card
  global dealer_card
  global your_card2
  global your_card_total
  global game_started
  global dealer_total_card
  global game_running
  if "who is cool" in f"{user_message}":
    return f''' yoni is  NOT cool
    '''
  elif "roll" in f"{user_message}":
        return f''' {random.randint(1 , 100)}

    '''
  elif "sing" in f"{user_message}":
        song = random.randint(1,2)
        if  song == 1:
          return f'''
Wheels on the bus goes round and round, round and round, round and round!
    '''
        if song == 2:
          return ''' Old MacDonald had a farm. E-I-E-I-O. And on that farm he had a pig. E-I-E-I-O.
'''
  elif "blackjack dealer" in f"{user_message,user_name}":

    dealer = user_name  

    return f'''  {user_name} is now dealer 
'''
  elif "blackjack player" in f"{user_message,user_name}":

    player = user_name  

    return f'''  {user_name} is now player 
'''
  elif "who is what" in f"{user_message,user_name}":

    return f'''{dealer} is dealer and {player} is player
     '''
  elif "start BJ" in f"{user_message}":
    balance = 100000

    BJ_started = True
    return f'''  starting BJ
you start with {balance}

     '''
  elif "balance" in f"{user_message}":
    return f'''{balance}
    '''
  elif "input" in f"{user_message,user_name}" and user_name == player and BJ_started == True :
    number = user_message[12:]
    number = int(number)
    if number > balance:
       return ''' you are broke 
      '''
    elif number < balance and number > 0:
      balance = balance - number
      game_started = True
      return f'''your new balance is {balance}

      '''
  elif "gamble" in f"{user_message,user_name}" and game_started == True and user_name == player and BJ_started == True:
      your_card =random.choice(card)
      your_card =  int(f"{your_card}")
      your_card2 = random.choice(card)
      your_card2 =  int(f"{your_card2}")
      dealer_card = random.choice(card)
      your_card_total = your_card + your_card2
      dealer_total_card = dealer_card
      game_running = True
      game_started = False
      return f''' you got {your_card}, and a {your_card2} total number is {your_card_total}
dealer got {dealer_card}
      '''
  elif "hit" in f"{user_message,user_name}" and game_running == True and user_name == player:
    your_card = random.choice(card)
    your_card_total = your_card_total + your_card
    if your_card_total > 21:
      number = 0
      your_card_total = 0
      return f''' you rolled a {your_card} and u busted.
      '''

    
    if your_card_total <= 21:
       return f''' you rolled a {your_card} and your total is {your_card_total}
  '''
  elif "stand" in f"{user_message,user_name}" and game_running == True and user_name == player :
    yoni_is_cool = True
    game_running == False
    for loop in range(100):
      dealer_card = random.choice(card)
      dealer_total_card = dealer_total_card + dealer_card
      if dealer_total_card > 21:
        balance = balance + number * 2
        number = 0
        yoni_is_cool = False
        return f''' dealer has  rolled a total of {dealer_total_card} and has busted 
      your new balance is {balance}
      '''
      elif dealer_total_card > 17 and dealer_total_card < your_card_total:
        
        balance = balance + number * 2
        number = 0
        return f''' dealer rolled a {dealer_total_card} and did not reach players number
        your new balance is {balance}
'''
      elif dealer_total_card > your_card_total and dealer_total_card < 22:
        
        number = 0
        return f''' dealer has rolled a {dealer_total_card} and has won.
'''


  

   