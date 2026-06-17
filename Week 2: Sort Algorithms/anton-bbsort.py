from dataclasses import dataclass
import random
@dataclass
class card():
    suit : str = ''
    value : int = 0

def build_deck():
    # setup all cards and return ten of them
    thesecards = [card() for index in range(52)]
    suits = ['hearts', 'clubs','diamonds','spades']
    count = 0
    for s in range(0,4):
        for index in range(1,14):
            thesecards[count].suit = suits[s]
            thesecards[count].value = index
            count += 1
    return thesecards

def draw_cards(thesecards):
    dealtcards = [card() for index in range(10)]
    selectednums = []
    # pick 10 to return
    for index in range(10):
        selectednum = random.randint(0,51)
        while selectednum in selectednums:
            selectednum = random.randint(0,51)
        selectednums.append(selectednum)
        dealtcards[index] = thesecards[selectednum]
    return dealtcards

def display_cards(cardarray):
    for index in range(len(cardarray)):
        output = cardarray[index].suit
        output = output + " : " + str(cardarray[index].value)
        print(output)

def init_size(deck):
    suits = ['hearts', 'clubs', 'diamonds','spades']
    for card in deck:
        card.size = card.value + (suits.index(card.suit)+1)*0.1

def sort_cards(deck):
    swaps = 0

    current = 1

    while current < len(deck):
        position = current
        if deck[position].size < deck[position-1].size and position > 0:
            while deck[position].size < deck[position-1].size and position > 0:
                deck[position], deck[position-1] = deck[position-1], deck[position]
                position -= 1

                display_cards(deck)
                print()

                swaps += 1
        else:
            print("No swap was made.")
            print()

        current += 1

    return deck

    


# main program
cards = [card() for index in range(10)]
allcards = [card() for index in range(52)]

allcards = build_deck()
cards = draw_cards(allcards)

init_size(cards)
sort_cards(cards)
display_cards(cards)
