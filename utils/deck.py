import random
def create_card(rank:str,suite:str) -> dict:
    card={"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
    type=["H","C","D","S"]
    if suite in type:
        return {"rank":rank,"suite":suite,"value":card[rank]}
def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card["value"] > p2_card["value"]:
        return 'p1'
    elif p1_card["value"] < p2_card["value"]:
        return 'p2'
    else:
        return 'WAR'
def create_deck() -> list[dict]:
    cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13,
            "A": 14}
    suit = ["H", "C", "D", "S"]
    full_desc=[]
    for type in suit:
        for card in cards:
            full_desc.append({type:card})
    return full_desc
def shuffle(deck:list[dict]) -> list[dict]:
    for i in range(1000):
        index1=random.randint(1,len(deck)-1)
        index2=random.randint(1,len(deck)-1)
        if deck[index1]== deck[index2]:
            continue
        deck[index1], deck[index2]=deck[index2],deck[index1]
    return deck
