lines = []
with open('04/input.txt', 'r') as file:
    lines = [line.strip() for line in file]

result = 0
scratchcards = 203

for line in lines:
    winners = []
    card_and_winners, n_scratchcards = line.split('| ')
    card_id, n_winners = card_and_winners.split(': ')
    card_id = card_id[5:]
    n_winners = n_winners.split()
    n_scratchcards = n_scratchcards.split()
    for n in n_scratchcards:
        if n in n_winners:
            winners.append(n)
    if len(winners) > 0:
        result += 2 ** (len(winners) - 1)

