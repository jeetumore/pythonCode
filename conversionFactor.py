# Example Facts (Conversion Factors):
# 1 meter (m) = 3.28 feet (ft)
# 1 foot (ft) = 12 inches (in)
# 1 hour (hr) = 60 minutes (min)
# 1 minute (min) = 60 seconds (sec)



conversionFactors = {
    'm_to_ft': 3.28,
    'ft_to_in': 12,
    'hr_to_min': 60,
    'min_to_sec': 60
}

def converMeterToinch(meter):
    feet = meter * conversionFactors['m_to_ft']
    inch = feet * conversionFactors['ft_to_in']
    return inch

def converInchtoMeter(inch):
    feet = inch / conversionFactors['ft_to_in']
    meter = feet / conversionFactors['m_to_ft']
    return meter

def are_the_compatible(unit1, unit2):
    compatible_list = ['m', 'ft', 'in', 'hr', 'min', 'sec']
    return unit1 in compatible_list and unit2 in compatible_list

def convert_units(value, from_unit, to_unit):
    if from_unit == 'm' and to_unit == 'in':
        return converMeterToinch(value)
    elif from_unit == 'in' and to_unit == 'm':
        return converInchtoMeter(value)
    else:
        if not are_the_compatible(from_unit, to_unit):
            print(" not conpatible")
        else:
            print("not convertable ")

print(f"4 meters = { convert_units(4, 'm', 'in')} inches " )
print(f"13 inches = {convert_units(13, 'in', 'hr')} hours")