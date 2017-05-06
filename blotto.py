# blotto.py
#
# Basic data structures for the blotto game
#


import pdb

# Returns the tuple of (wins, draws, losses) for strategy_a.
def run_blotto_game(strategy_a, strategy_b):
    num_battlefields = len(strategy_a)
    wins = 0; draws = 0; losses = 0
    for i in range(num_battlefields):
        if (strategy_b == None):
            print("strategy a ", strategy_a)
            print("strategy b ", strategy_b)
        
        if (strategy_a[i] > strategy_b[i]):
            wins += 1
        elif (strategy_a[i] == strategy_b[i]):
            draws += 1
        else:
            losses += 1
    return (wins, draws, losses)
    

def get_winner(strategy_a, strategy_b):
    (wins, _, losses) = run_blotto_game(strategy_a, strategy_b)
    if (wins > losses):
        return strategy_a
    elif (losses > wins):
        return strategy_b
    return None
    
def best_response_one_day(enemy_strategy, num_soldiers=None):
    current_soldiers = num_soldiers
    if (num_soldiers == None):
        current_soldiers = sum(enemy_strategy)
    sorted_fields = [(field, i) for (i,field) in enumerate(enemy_strategy)]
    sorted_fields.sort(key=lambda x: x[0])
    ######
    #Actual best response
    best_response = [0] * len(enemy_strategy)
    for (bf,i) in sorted_fields:
        if (bf+1 >= current_soldiers):
            best_response[i] = current_soldiers
            return best_response
        best_response[i] = bf + 1;
        current_soldiers -= (bf+1)
    ######
    
    

def numSoldiers(strategy):
    n = 0
    for i in range(0, len(strategy)):
        n += strategy[i]
    return n


def best_response_with_discount(player_strategy, enemy_strategy):
    if (get_winner(player_strategy, enemy_strategy) == player_strategy):
        return player_strategy
    return best_response_one_day(enemy_strategy, sum(player_strategy) - 1)
    
    
    
def numSoldiers(strategy):
    return sum(strategy)

    
def enumerate_strategies1(num_soldiers, num_battlefields, strategy, l):
    if (num_soldiers == 0):
        l.append(strategy + num_battlefields*[0])
        return l
    if (num_battlefields == 1):
        l.append(strategy + [num_soldiers])
        return l
    for i in range(0, num_soldiers + 1):
        enumerate_strategies1(num_soldiers - i, num_battlefields - 1, strategy + [i], l)
    return l
    
def enumerate_strategies(num_soldiers, num_battlefields):
    def recursiveHelper(soldiers, battlefields):
        if (soldiers == 0):
            yield [0]*battlefields
        if (battlefields == 1):
            yield [soldiers]
        for i in range(soldiers+1):
            for substrat in recursiveHelper(soldiers - i   , battlefields-1):
                yield [i] + substrat
    import pdb; pdb.set_trace()    
    for strategy in recursiveHelper(num_soldiers, num_battlefields) :
        yield strategy

        
def respond(player_strategy, enemy_strategy):
    altMove = best_response_one_day(enemy_strategy, numSoldiers(player_strategy)-1)
    curScore = run_blotto_game(player_strategy, enemy_strategy)
    score = run_blotto_game(altMove, enemy_strategy)
    if (score[0] - score[2] > curScore[0] - curScore[2]):
        return altMove
    else:
        return player_strategy
    

#very brute force level k response, currently only works for 4 battlefields
def levelkResponse(player_strategy, enemy_strategy, k):
    if (k <= 0):
        return respond(player_strategy, enemy_strategy)
    if (k == 1):
        n = numSoldiers(player_strategy)-1
        bestStrat = player_strategy
        bestScore = run_blotto_game(bestStrat, respond(enemy_strategy, bestStrat))
        for strat in enumerate_strategies1(n, len(player_strategy), [],[]):
            score = run_blotto_game(strat, respond(enemy_strategy, strat))
            if (score[0] - score[2] > bestScore[0] - bestScore[2]):
                bestStrat = strat
                bestScore = score
        return bestStrat
    if (k > 1):
        n = numSoldiers(player_strategy)-1
        bestStrat = player_strategy
        bestScore = run_blotto_game(bestStrat, levelkResponse(enemy_strategy, bestStrat, k-1))
        for strat in enumerate_strategies1(n, len(player_strategy), [],[]):
            enemy_strat = levelkResponse(enemy_strategy, strat, k-1)
            score = run_blotto_game(strat, enemy_strat)
            if (score[0] - score[2] > bestScore[0] - bestScore[2]):
                bestStrat = strat
                bestScore = score
        return bestStrat
    
#Question: can you ever have a scenario where, when the curtain is lifted, both players would like to move first?
#i.e. the loser would like to mitigate their losses and the winner would like to pre-empt that?
#Statement: at any point in time, if you're going to switch moves, you might as well switch to your current best response
#True or false?
#Idea: number of troops left at end counts towards utility? Either a significant amount or just as a tiebreaker
#becomes more similar to an auction when arbitrary number of people in war

