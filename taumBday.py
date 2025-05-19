


def taumBday(b, w, bc, wc, z):

    if bc + z < wc:
        total_cost = b * bc + w * (bc + z)
    elif wc + z < bc:
        total_cost = w * wc + b * ( wc + z)
    else:
        total_cost = w * wc + b *  bc


    return  total_cost





def taumBday(b, w, bc, wc, z):
    # Calculate costs based on conversion conditions
    if bc + z < wc:
        # Buy all as black, convert some to white
        total_cost = b * bc + w * (bc + z)
    elif wc + z < bc:
        # Buy all as white, convert some to black
        total_cost = w * wc + b * (wc + z)
    else:
        # Buy black and white directly
        total_cost = b * bc + w * wc

    return total_cost




taumBday(10, 10, 1, 1, 1)

print(taumBday(10, 10, 1, 1, 1))