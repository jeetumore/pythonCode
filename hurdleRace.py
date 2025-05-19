
def hurdleRace(k, height):
    # Write your code here
    doses =  max(height) - k
    return doses if doses > 0 else 0


hurdleRace(4, [1, 6, 3, 5, 2]) # 2