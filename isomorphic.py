

def isomorphic(s, t):

    s_to_t = {}
    t_to_s = {}

    for char_s, char_t in zip(s, t):
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False

        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False

        s_to_t[char_s] = char_t
        print(s_to_t)
        t_to_s[char_t] = char_s
        print(t_to_s)

    return True


isomorphic("egg", "add")



def are_units_compatible(unit1, unit2):
    compatible_units = ['m', 'ft', 'in', 'hr', 'min', 'sec']
    ans= unit1 in compatible_units and unit2 in compatible_units
    return ans

if  not are_units_compatible('in', 'hr'):
    print( "not convertible!")
else:
    print("ok")





def isomorphic(s, t):


    s_to_t = {}
    t_to_s = {}

    for s, t in zip(s, t):
        if s in s_to_t:
            if s_to_t[s] != t:
                return False
        if t in t_to_s:
            if t_to_s[t] != s:
                return False
        s_to_t[s] = t
        t_to_s[t] = s

    return True





















