from utils.deck import *
from game_logic.game import *

if __name__=="__main__":
    game=init_game()
    raund=play_round()
    while raund["hand"]:


