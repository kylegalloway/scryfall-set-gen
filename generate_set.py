import sys
import requests


def main():
    print("Pulling set: " + sys.argv[1])

    base_url = "https://api.scryfall.com/cards/search?order=set&unique=prints"
    set_param = "&q=set:" + sys.argv[1]
    full_url = base_url + set_param

    response = make_request(full_url)
    print_cards_as_list(response["data"])

    while response["has_more"]:
        response = make_request(response["next_page"])
        print_cards_as_list(response["data"])


def make_request(url):
    response = requests.get(url)
    return response.json()


def print_cards_as_list(cards):
    for card in cards:
        print("0 " + card["name"] + " (" + card["set"] + ")" + " " + card["collector_number"])


if __name__ == "__main__":
    main()
