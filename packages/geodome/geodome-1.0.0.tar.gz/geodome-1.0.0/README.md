## Geodesic Dome

Geodome is a python library that enables users to manipulate a 3D geodesic dome.
The library provides the capability for users to store data in vertices and
manipulate the overall structure of the dome. There are options to tessellate
the entire dome, partially tessellate the dome and find neighbouring vertices.
The library provides various powerful commands to enable these functions through
a user-facing class wrapper. 

The library prioritises efficiency by compiling through [Numba](https://numba.pydata.org/).

## Installation
To install our library please use the following command:

```
$ pip install geodome
```

## Basic Usage
An example of how to instantiate a Geodesic Dome class can be found below:

```python
from geodome import GeodesicDome

gd = GeodesicDome()

# Futher operations here
```

Documentation for the available class wrapper and its related methods can be
found [here](https://geodomedocs.netlify.app/).

*This python library was created as a University of Sydney capstone unit under
the direction of the School of Computer Science*