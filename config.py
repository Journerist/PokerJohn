import os

from poker_states import PokerStates

other_player_count = 9
state_size = len(PokerStates)*9
train_game_count = 100
batch_size = 32
output_dir = 'model_output/poker'
if not os.path.exists(output_dir):
    os.makedir(output_dir)

