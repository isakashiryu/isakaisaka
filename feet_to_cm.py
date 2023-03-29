def feet_to_cm(feet, inch):
    cm_per_inch = 2.54
    inch_per_foot = 12
    cm_per_foot = inch_per_foot * cm_per_inch
    total_cm = feet * cm_per_foot + inch * cm_per_inch
    return total_cm

# 例
feet = 5
inches = 8
centimeters = feet_to_cm(feet, inches)
print(centimeters)