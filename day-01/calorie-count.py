data = './calories-in.txt'


def get_calories():
    calories = open(data, "r").read().split("\n\n")
    num = []
    for cal in calories:
        num.append(sum([int(x) for x in cal.split("\n")]))
    return num


print(max(get_calories()))
print(sum(sorted(get_calories())[-3:]))
