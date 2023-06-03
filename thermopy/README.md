# ThermoPy

Author: Jacopo Cocomello
Date: 21 May 2021

This is a simple project through which I'm trying to learn more Python programming making use of a theory that I particularly like, Thermodynamics.

The project may be reused for educational purposes, for example as a mean for students to become more used to coding and thermodynamics.

## Units and standards

All systems will be considered to be ideal gases at equilibrium and all processes will be considered to proceed through intermediate thermalized steps.

I will use SI units:

-   Temperature is in Kelvin 
-   Energy is in Joules
-   Length is in meters
-   Mass is in kilograms
-   Time is in seconds

All processes and systems will take place and exist in three dimensional space.

## Structure of the project

```
thermopy
├── main.py
├── src
│   ├── laws.py
│   └── system_class.py
└── test
    ├── test.py
```

## Thermodynamics system class

**Types of system**:

-   open: `open, o`
-   closed: `closed, c`
-   thermally isolated: `t-isolated, ti`
-   mechanically isolated: `m-isolated, mi`
-   isolated: `isolated, i`

**Type of boundaries**

-   real: `real, r`
-   imaginary: `imaginary, i`
-   fixed: `fixed, f`
-   movable: `movable, m`

Define boundaries of the system by first stating the degree of reality of the boundary and then the degree of mobility of the same.

The boundary object is a list of dimension ($3 \times 2 \times 2$), for a cubic box is considered and each of the $6$ box sides has to be defined.

*Structure of the boundary object*

```
|x                |y                |z
|top     |bottom  |top     |bottom  |top     |bottom
|r/i f/m |r/i f/m |r/i f/m |r/i f/m |r/i f/m |r/i f/m
```

**State quantities**:

-   internal energy
-   entropy
-   pressure
-   temperature
-   volume
-   mass
-   particle number

**Processes**

-   adiabatic
-   isobaric
-   isochoric
-   isothermal

**System-specific properties**

-   molar specific heat at constant volume/pressure