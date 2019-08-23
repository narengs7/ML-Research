#!/usr/bin/env python3

import random

ROCK, PAPER, SCISSORS = 0, 1, 2
NUM_ACTIONS = 3 # Defining total actions that can take
regret_sum, strategry, strategry_sum = [0.0]*3, [0.0]*3, [0.0]*3  # Assign arr of size 3 to regret, statagry and its sum
opp_strategy = [0.4, 0.3, 0.3]

RPS_MATRIX = [
    [[0, 0], [1, -1], [-1, 1]],
    [[-1, 1], [0, 0], [1, -1]],
    [[1, -1], [-1, 1], [0, 0]]
]

def checkRohambo(p1,p2):
    '''
    To evaluate who won and return respective value
    :param p1:
    :param p2:
    :return p1 and p2 win/lose value:
    '''
    return RPS_MATRIX[p2][p1]

def getStrategy():
    '''
        to generate mixed stategies through regret matching
    :return strategy:
    '''
    normalizing_sum = 0.0
    for i in range(NUM_ACTIONS):
        strategry[i] = regret_sum[i] > 0 and regret_sum[i] or 0.0
        normalizing_sum += strategry[i]  # Normalization sum can be positive or negative based on regret

    # In cases where normalization becomes negative due to regrets the strategy needs to be updated to maintain uniform
    for i in range(NUM_ACTIONS):
        if normalizing_sum > 0 :
            strategry[i] /= normalizing_sum
        else:
            strategry[i] = 1.0/NUM_ACTIONS
        strategry_sum[i] += strategry[i]

    return strategry

def getAvgStrategy():
    avg_strategy = [0.0]*3
    norm_sum = 0.0
    for i in range(NUM_ACTIONS):
        norm_sum += strategry_sum[i]

    for i in range(NUM_ACTIONS):
        if norm_sum >0:
            avg_strategy[i] = strategry_sum[i]/norm_sum
        else:
            avg_strategy[i] = 1.0/NUM_ACTIONS;
    return avg_strategy


def getAction(strat):
    '''
    Action which is to be performed using the strategy planned
    :param strat:
    :return head or tain or scissor (either one):
    '''
    r, a, cum_prob = random.randint(0, 3), 0, 0.0
    while a < NUM_ACTIONS-1:
        cum_prob += strat[a]
        if r < cum_prob:
            break
        a = a + 1
    return a



def train(iteration):
    '''
    Triaing my program
    :param iteration:
    :return:
    '''
    action_utility = [0.0, 0.0, 0.0]
    for i in range(iteration):
        # Regret Matching mixed strategy
        strat = getStrategy()
        my_action = getAction(strat)
        opp_action = getAction(opp_strategy)

        action_utility[opp_action] = 0

        action_utility[opp_action == NUM_ACTIONS - 1 and 0 or opp_action-1] = 1
        action_utility[opp_action == 0 and NUM_ACTIONS - 1 or opp_action - 1] = 1

        for j in range(NUM_ACTIONS):
            regret_sum[j] += action_utility[j] - action_utility[my_action]

train(100000)
print(getAvgStrategy())

