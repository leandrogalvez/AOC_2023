lines = []
with open('02/input.txt', 'r') as file:
    lines = [line.strip() for line in file]

maximos = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
result = 0
valid_games = []

for line in lines:
    game, match = line.split(':')
    matches = match.split(';')
    valid = True
    for match in matches:
        partida = match.split(',')
        for cube in partida:
            num, color = cube.strip().split(' ')
            if int(num) > maximos[color]:
                print(num, color)
                valid = False
    if valid:
        valid_games.append(game.replace("Game ", ""))
        print(game.replace("Game ", ""))
for valid_game in valid_games:
    result += int(valid_game)

print(result)