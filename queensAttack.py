
#
def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here

    directions = {
        "up":  n - r_q,
        "down": r_q - 1,
        "right": n - c_q,
        "left": c_q -1,
        "up-right": min(n -r_q, n - c_q),
        "up-left": min(n - r_q, c_q - 1),
        "down-right": min(r_q - 1, n - c_q),
        "down-left": min(r_q -1 , c_q - 1)
    }

    for obstacle in obstacles:
        r_o, c_o = obstacle
        if c_o == c_q:
            if r_o > r_q:
                directions["up"] = min(directions["up"], r_o - r_q - 1)
            else:
                directions["down"] = min(directions["down"], r_q - r_o - 1)
        elif r_o == r_q:
            if c_o > c_q:
                directions["right"] = min(directions["right"], c_o - c_q -1)
            else:
                directions["left"] = min(directions["left"], c_q - c_o -1 )
        elif abs(r_o - r_q) == abs(c_o - c_q):
            if r_o > r_q  and c_o > c_q:
                directions["up-right"] = min(directions["up-right"], r_o - r_q - 1)
            elif r_o > r_q and c_o < c_q:
                directions["up-left"] = min(directions["up-left"], r_o - r_q -1)
            elif r_o < r_q and c_o > c_q:
                directions["down-right"] = min(directions["down-right"], r_q - r_o -1)
            elif r_o < r_q and c_o < c_q:
                directions["down-left"] = min(directions["down-left"], r_q - r_o -1)





    total_attack_squares = sum(directions.values())


    print(total_attack_squares)



def queensAttack(n, k, r_q, c_q, obstacles):

    directions = {
        "up" : n - r_q,
        "down": r_q - 1,
        "right": n - c_q,
        "left": c_q -1,
        "up-right": min(n - c_q, r_q -1),
        "up-left": min(n - c_q, c_q - 1),
        "down-right": min(r_q -1, n - c_q),
        "down-left": min(r_q -1, c_q -1)

    }


    for obstacle in obstacles:
        r_o, c_o = obstacle

        if c_o == c_q:
            if r_o > r_q:
                directions["up"] = min(directions["up"], r_o - r_q -1)
            else:
                directions["down"] = min(directions["up"], r_q - r_o -1)
        elif r_o == r_q:
            if c_o > c_q:
                directions["right"] = min(directions["right"], c_o - c_q -1)
            else:
                directions["left"] = min(directions["left"], c_q - r_o -1)
        elif abs(r_o - r_q) == abs(c_o - c_q):
            if r_o > r_q  and c_o > c_q:
                directions["up-right"] = min(directions["up-right"], r_o - r_q - 1)
            elif r_o > r_q and c_o < c_q:
                directions["up-left"] = min(directions["up-left"], r_o - r_q - 1)
            elif r_o < r_q and c_o > c_q:
                directions["down-right"] = min(directions["down-right"], r_q -r_o -1)
            elif r_o < r_q and c_o < c_q:
                directions["down-left"] = min(directions["down-left"], r_q -r_o -1)





    total_attack_squares = sum(directions.values())
    print(total_attack_squares)


queensAttack(4, 0, 4, 4 , [])

