from utils.deck import create_deck, shuffle
def create_player(name:str) -> dict:
    player=name
    if not name:
        player="AI"
    hand=[]
    wom_pile=[]
    return {"name":player,"hand":hand,"wom_pile":wom_pile}

def init_game()->dict:
    p1=create_player("Yosef")
    p2=create_player(None)
    d = create_deck()
    d = shuffle(d)
    p1["hand"]=d[:27]
    p2["hand"]=d[27:]
    return {"deck":d,"player1":p1,"player2":p2}

def play_round(p1:dict,p2:dict):
    pleyers=init_game()
    player1=pleyers["player1"].pop("hand")
    player2=pleyers["player2"].pop("hand")
    if player1> player2:
        pleyers["player1"].update("wom_pile")
    if player1 < player2:
        pleyers["player2"].update("wom_pile")
    else:
        pass