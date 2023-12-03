lines = []
with open('01/input.txt', 'r') as file:
    lines = [line.strip() for line in file]

numeros = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
def letter_to_num(lines):
    new_lines = []
    for line in lines:
        for num in numeros:
            line = line.replace(num, num+str(numeros.get(num))+num) 
        new_lines.append(line)
    return new_lines

suma = 0

for line in letter_to_num(lines):
    nums = []
    for char in line:
        if char.isdigit():
            nums.append(char)
    nums = nums[0] + nums[-1]
    suma += int(nums)

print(suma)