### Time it
Use %timeit within a python shell to time functionality  
`import numpy as np`  
`%timeit n = np.random.rand(1000)`  
`7.82 µs ± 112 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)`  
Note: it cannot be used in a script
### Built in tools
Built in tools such as `itertools` and `collections` are faster 
than manual implementations
### Eliminate Loops
Alternatives
* Set
* Collections
* Numpy/Pandas
