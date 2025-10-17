# Naomi Puyleart
# 10/17/25
# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.
# The mainline then displays the distance.
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)

import math

def distance_coordinates(cord1, cord2):
    distance = math.sqrt((cord1[0] - cord2[0])**2 + (cord1[1] - cord2[1])**2 + (cord1[2] - cord2[2])**2)
    return distance

def main():
    cord1_tuple = tuple(map(float, input("Enter the first coordinate separated by spaces: ").split()))
    cord2_tuple = tuple(map(float, input("Enter the second coordinate separated by spaces: ").split()))
    print("This is the first coordinate you entered: ", cord1_tuple)
    print("This is the second coordinate you entered: ", cord2_tuple)

    if len(cord1_tuple) != 3 or len(cord2_tuple) != 3:
        print("Please rerun and enter valid coordinates (3 values only).")
    else:
        distance = distance_coordinates(cord1_tuple, cord2_tuple)
        print("The distance between the two coordinates is: ", distance)

if __name__ == "__main__":
    main()