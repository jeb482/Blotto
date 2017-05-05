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