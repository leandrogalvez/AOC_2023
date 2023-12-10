lines = []
with open('02/input.txt', 'r') as file:
    lines = [line.strip() for line in file]

maximos = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
result = 0
potencia = 1
valid_games = []
for line in lines:
    game, match = line.split(':')
    matches = match.split(';')
    valid = True
    for match in matches:
        partida = match.split(',')
        min_num_red = 1
        min_num_green = 1
        min_num_blue = 1
        for cube in partida:
            num, color = cube.strip().split(' ')
            
            if int(num) > maximos[color]:
                valid = False
            if int(num) <= min_num_red and color == "red":
                min_num_red = int(num)
            else:
                continue
            if int(num) <= min_num_green and color == "green":
                min_num_green = int(num)
            else:
                continue
            if int(num) <= min_num_blue and color == "blue":
                min_num_blue = int(num)
            else:
                continue
            
            potencia *= min_num_red * min_num_green * min_num_blue    
    if valid:
        valid_games.append(game.replace("Game ", ""))
for valid_game in valid_games:
    result += int(valid_game)

print(potencia)