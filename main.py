from pypokerengine.api.game import setup_config, start_poker

from john_player import JohnPlayer

config = setup_config(max_round=10, initial_stack=100, small_blind_amount=5)
config.register_player(name="p1", algorithm=JohnPlayer())
config.register_player(name="p2", algorithm=JohnPlayer())
config.register_player(name="p3", algorithm=JohnPlayer())
game_result = start_poker(config, verbose=1)
