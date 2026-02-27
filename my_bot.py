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
global dealer
global player

# def            respond(user_message, user_name):
#   return f"""you said my name!!
#   {user_message.replace("robot", user_name)}"""
# cards =["1","2","3","4","5","6","7","8","9","jack","queen","king", "ace"]
card = [1, 2, 3, 4, 5 ,6 ,7, 8, 9, 10, 10, 10, 10]
def respond(user_message,user_name):
  if "who is cool" in f"{user_message}":
    return f''' yoni is cool
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
    global dealer
    dealer = user_name  

    return f'''  {user_name} is now dealer 
'''
  elif "blackjack player" in f"{user_message,user_name}":
    global player
    player = user_name  

    return f'''  {user_name} is now player 
'''
  elif "who is what" in f"{user_message,user_name}":

    return f'''{dealer} is dealer and {player} is player
     '''


  
# def respond(user_message,user_name):
#   if "is yoni cool" in user_message:
#    return f''' u said my name!!!
#     {user_message.replace("robot", user_name)}'''
   