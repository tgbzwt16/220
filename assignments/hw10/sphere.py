"""
Name: Thomas Thornley
<ProgramName>.py

Problem: Creating sphere class.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math


class Sphere:
    def __init__(self, radius):
        self.radius = radius
        self.area = 0

    def get_radius(self):
        return self.radius

    def surface_area(self):
        sphere_area = 4 * math.pi * (self.radius ** 2)
        return sphere_area

    def volume(self):
        sphere_volume = (4.0 / 3.0) * math.pi * (self.radius ** 3.0)
        return sphere_volume
