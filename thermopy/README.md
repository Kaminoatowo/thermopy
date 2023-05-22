# ThermoPy

Author: Jacopo Cocomello
Date: 21 May 2021

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

**State quantities**:

-   energy
    -   enthalpy
    -   internal energy
    -   Gibbs free energy
    -   Helmholtz free energy
-   entropy
-   pressure
-   temperature
-   volume
-   mass
-   particle number