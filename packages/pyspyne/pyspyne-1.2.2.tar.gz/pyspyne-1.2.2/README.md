# Spyne v1.0.0

The all-in-one Python package.
****
## Setup

In your terminal:
```bash
$ pip install pyspyne
```
In the python file:

```python
import pyspyne
```
***
## Modules

####Math

You can use all the methods in the regular Python Math module in Spyne Math
```python
math = spyne.math
my_equation = math.Equation("2 * x")
```
Creates a new Equation object for the Graphr Module
***
####Graphr
```python
graphr = spyne.graphr
graphr.draw(my_equation, units=1)
```
Draws a turtle graph based on the equation\
Parameters:
- my_equation (Required): Equation object from Spyne Math
- units (Default=1): Graph units

***
###Extended documentation coming soon!












