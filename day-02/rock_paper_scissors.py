data = './data.txt'

lose = 0
draw = 3
win = 6
rock = 1
paper = 2
scissor = 3
X = rock
Y = paper
Z = scissor

score = 0

# Part 1
rps = (open(data, "r").read()).split("\n")
for line in rps:
    # Draw
    if (line == 'A X') or (line == 'B Y') or (line == 'C Z'):
        score = score + draw
        if line == 'A X':
            score = score + X
        elif line == 'B Y':
            score = score + Y
        elif line == 'C Z':
            score = score + Z
    # Win
    elif (line == 'A Y') or (line == 'B Z') or (line == 'C X'):
        score = score + win
        if line == 'A Y':
            score = score + Y
        elif line == 'B Z':
            score = score + Z
        elif line == 'C X':
            score = score + X
    # lose
    else:
        score = score + lose
        if line == 'A Z':
            score = score + Z
        elif line == 'B X':
            score = score + X
        elif line == 'C Y':
            score = score + Y
print(f"Part 1: {score}")


score = 0
rps = (open(data, "r").read()).split("\n")
for line in rps:
    # Draw
    if (line == 'A Y') or (line == 'B Y') or (line == 'C Y'):
        score = score + draw
        if line == 'A Y':
            score = score + X
        elif line == 'B Y':
            score = score + Y
        elif line == 'C Y':
            score = score + Z
    # Win
    elif (line == 'A Z') or (line == 'B Z') or (line == 'C Z'):
        score = score + win
        if line == 'A Z':
            score = score + Y
        elif line == 'B Z':
            score = score + Z
        elif line == 'C Z':
            score = score + X
    # lose
    else:
        score = score + lose
        if line == 'A X':
            score = score + Z
        elif line == 'B X':
            score = score + X
        elif line == 'C X':
            score = score + Y
print(f"Part 2: {score}")
