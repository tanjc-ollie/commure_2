import requests

mapped_values = {"ACE":1, "JACK": 11, "QUEEN": 12, "KING": 13}

def map_card_values(cards):
    return [{
        "value": mapped_values.get(card["value"], int(card["value"])),
        "suit": card["suit"]
        } for card in cards]

def draw_cards():
    url = "https://www.deckofcardsapi.com/api/deck/new/draw/?count=5"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        cards = list(map(lambda card: {"value": card["value"], "suit": card["suit"]}, data["cards"]))
        cards = map_card_values(cards)
        cards.sort(key=lambda card: card["value"])

        reversed_mapped_values = {v: k for k, v in mapped_values.items()}
        for card in cards:
            value = reversed_mapped_values[card["value"]] if card["value"] in reversed_mapped_values else card["value"]
            print(f"{value} of {card["suit"]}")
        
    else:
        print(response.reason)

    print("done")

def winning_condition(cards: list[str]) -> bool:
    cards = map_card_values(cards)
    cards.sort(key=lambda card: card["value"])

    for i in range(len(cards) - 1):
        val = cards[i]["value"]
        val2 = cards[i + 1]["value"]
        if val2 - val > 1:
            return False

    return True
    

if __name__ == "__main__":
    print("starting")

    draw_cards()
