# scryfall-set-gen

Generates a list of all prints in a set for ease of importing to collection. Uses Scryfall API.

## Requirements

`pip install -r requirements.txt`

## Usage

`python3 generate_set.py <code>`

To save to a file:

`python3 generate_set.py <code> > <filename>`

## Output Format

`AMOUNT CARDNAME (SETCODE) NUMBER`

The modifier `*F*` can be added after a line to indicate a foil. See https://www.moxfield.com/help/creating-decks
