import numpy as np
import random
import mchmm as mc

def player1(prev_play, opponent_history=[]):
  # states = ['R', 'P', 'S']
  ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
  transitions = [["RR", "RP", "RS"], ["PR", "PP", "PS"], ["SR", "SP", "SS"]]
  guess = ""
  prob = 1

  if prev_play == '':
    # prev_play = random.choice(states)
    prev_play = 'R'
    opponent_history.append('S')
    opponent_history.append('P')

  opponent_history.append(prev_play)
  chain = mc.MarkovChain().from_data(opponent_history)
  transitionMatrix = chain.observed_p_matrix

  if prev_play == 'R':
    change = np.random.choice(transitions[0], replace=True, p=transitionMatrix[0])
    if change == "RR":
      prob = prob * transitionMatrix[0][0]
      guess = "R"
    elif change == "RP":
      prob = prob * transitionMatrix[0][1]
      guess = "P"
    elif change == "RS":
      prob = prob * transitionMatrix[0][2]
      guess = "S"

  elif prev_play == 'P':
    change = np.random.choice(transitions[1], replace=True, p=transitionMatrix[1])
    if change == "RR":
      prob = prob * transitionMatrix[1][0]
      guess = "R"
    elif change == "RP":
      prob = prob * transitionMatrix[1][1]
      guess = "P"
    elif change == "RS":
      prob = prob * transitionMatrix[1][2]
      guess = "S"

  elif prev_play == 'S':
    change = np.random.choice(transitions[2], replace=True, p=transitionMatrix[2])
    if change == "RR":
      prob = prob * transitionMatrix[2][0]
      guess = "R"
    elif change == "RP":
      prob = prob * transitionMatrix[2][1]
      guess = "R"
    elif change == "RS":
      prob = prob * transitionMatrix[2][2]
      guess = "S"

  return ideal_response.get(guess)

def player2(prev_play, opponent_history=[]):
  states = ['R', 'P', 'S']
  ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

  if prev_play == '':
    prev_play = 'S'
    i = 0
    while (i < 5):
      opponent_history.append(random.choice(states))
      i += 1

  opponent_history.append(prev_play)

  n = 3
  chain = mc.MarkovChain().from_data(opponent_history)
  transmatrix = chain.observed_p_matrix
  n_transmatrix = chain.n_order_matrix(transmatrix, order=n)
  index = np.where(chain.states == prev_play)[0][0]
  guess = chain.states[np.argmax(n_transmatrix[index])]
  return ideal_response[guess]