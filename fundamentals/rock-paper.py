def rps(p1, p2):
    if p1 == "scissors" and p2 == "paper" or p1 == "rock" and p2 == "scissiors" or p1 == "paper" and p2 == "rock":
        result = "Player 1 won!"
    elif p1 == "scissors" and p2 == "rock" or p1 == "rock" and p2 == "paper" or p1 == "paper" and p2 == "scissiors":
        result = "Player 2 won!"
    elif p1 == "paper" and p2 == "paper" or p1 == "rock" and p2 == "rock" or p1 == "scissiors" and p2 == "scissiors":
        result = "Draw"
    else:
        result = "Wrong"
    return result


p1 = input("player1: ")
p2 = input("plater2: ")
result = rps(p1, p2)
print(result)