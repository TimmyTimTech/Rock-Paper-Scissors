# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    freqs = {'R': 0, 'P': 0, 'S': 0}
    if len(opponent_history) > 2:
        for move in set(opponent_history[-3:]):
            freqs[move] += 1
        guess = max(freqs, key=freqs.get)
    else:
        guess = random.choice('RPS')
    return guess
