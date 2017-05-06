# blotto.py
#
# Basic data structures for the blotto game
#

# Returns the tuple of (wins, draws, losses) for strategy_a.
def run_blotto_game(strategy_a, strategy_b):
    num_battlefields = len(strategy_a)
    wins = 0; draws = 0; losses = 0
    for i in range(num_battlefields):
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
    

def best_response_with_discount(player_strategy, enemy_strategy)
    if (get_winner(player_strategy, enemy_strategy) == player_strategy)
        return player_strategy
    return best_response_one_day(enemy_strategy, sum(player_strategy) - 1)
    
    
    
def numSoldiers(strategy):
    return sum(strategy)

def allStrategies(num_soldiers, num_battlefields):
    def recursiveHelper(soldiers, battlefields):
        if (soldiers == 0)
            yield [0]*battlefields
        if (battlefields == 1)
            yield [soldiers]
        for i in range(soldiers+1)
            for substrat in recursiveHelper(soldiers - i, battlefields-1)
                yield [i] + substrat
        
    for strategy in recursiveHelper(num_soldiers, num_battlefields) 
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
        for i in range(0, n+1):
            for j in range(0, n+1-i):
                for l in range(0, n+1-i-j):
                    strat = [i, j, l, n-i-j-l]
                    score = run_blotto_game(strat, respond(enemy_strategy, strat))
                    if (score[0] - score[2] > bestScore[0] - bestScore[2]):
                        bestStrat = strat
                        bestScore = score
        return bestStrat
    #need better way to do this without brute force    
    #maybe start with total brute force and then try to notice a pattern?
    if (k > 1):
        return respond(player_strategy, levelkResponse(enemy_strategy, player_strategy, k-1))
    
#Question: can you ever have a scenario where, when the curtain is lifted, both players would like to move first?
#i.e. the loser would like to mitigate their losses and the winner would like to pre-empt that?
#Statement: at any point in time, if you're going to switch moves, you might as well switch to your current best response
#True or false?
#Idea: number of troops left at end counts towards utility? Either a significant amount or just as a tiebreaker
#becomes more similar to an auction when arbitrary number of people in war
    
    