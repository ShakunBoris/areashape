# areashape

areashape is a Python library for calculating areas of geometric shapes such as triangle and circle.

## Installation

To install the library locally, you can clone this repository:

```bash
git clone https://github.com/ShakunBoris/areashape.git
```

Then, navigate to the areashape directory and install the library using pip:

```bash
cd areashape
pip install .
```

## USAGE

Here is an example of how to use the library to calculate the area of a triangle:

``` python

import areashape as ash

print(ash.Triangle.area_by_sides(3,4, 5))
t = ash.Triangle((2,1), (3,6), (6,2))
c = ash.Circle(4)
print(ash.calculate_area(t))
print(ash.calculate_area(c))
print(t.area())
print(c.area())
print(t.is_right_angled)
print(t.right_angled_check)

```