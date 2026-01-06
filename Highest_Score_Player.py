n = int(input())

highest_score = -1
top_player = ""

for _ in range(n):
    data = input().split(',')
    name = data[0]
    score = int(data[1])

    if score > highest_score:
        highest_score = score
        top_player = name

print(top_player)
