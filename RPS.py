# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
import numpy as np
from itertools import product

# to make playorder contain longer combinations
n = 5
states = ['R', 'P', 'S']
combs = [''.join(comb) for comb in product(states, repeat=n)]

def player(prev_play, opponent_history=[], 
           play_order = [dict(zip(combs, [0]*len(combs)))]):
  # improvising on Abbey's Markov Chain
  global n
  ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}  

  # everyone chooses Rock as a default 1st prev_play -> counter
  if prev_play == '':
    prev_play = 'S'
  prediction = 'S'
  # don't forget to add the previous play to the buffer
  opponent_history.append(prev_play)
  
  # instead of abbey's last 2, use last n
  last_n = "".join(opponent_history[-n:])
  if len(last_n) == n:
      last_n_1 = "".join(opponent_history[-(n-1):])
      play_order[0][last_n] += 1
      
      potential_plays = [
          last_n_1 + "R",
          last_n_1 + "P",
          last_n_1 + "S" ]
      sub_order = {
          k: play_order[0][k]
          for k in potential_plays if k in play_order[0]
      }
      prediction = max(sub_order, key=sub_order.get)[-1:]
  else:
    prediction = prev_play
  return ideal_response[prediction]

  ## This is the default play strategy; uncomment this and comment above strategy to observe its success rate
  # opponent_history.append(prev_play)
  # guess = "R"
  # if len(opponent_history) > 2:
  #     guess = opponent_history[-2]

  # return guess
