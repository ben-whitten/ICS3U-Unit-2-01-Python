#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: September 2019
# This is a program which can find the area and perimeter or a circle.


# This is what finds the area and perimeter of the circle.
# Replace the two numbers at the end of lines 12, 14 and 15 with radius
# to continue.
import math


def main():
    print("If a circle has the demensions:")
    print("5cm x 3cm")
    print("")
    print("Then the area of the circle is {}cm^2" .format(math.pi*3**2))
    print("and the perimeter is {}cm" .format(2*math.pi*3))


if __name__ == "__main__":
    main()
