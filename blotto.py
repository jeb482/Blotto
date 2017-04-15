# blotto.py
#
# Basic data structures for the blotto game
#

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