Functions that takes a set of data points and finds a function to 
interpolate them. For both functions, you input a csv file that
contains the data points as two rows, with the x-values making up
the first row and the y-values making up the second row. The functions
will write the interpolating polynomial as a string to a file of
your choosing. It will also return the polynomial as a lambda so
you can easily plug numbers into it.

delimiter = ','

Interpolation Methods:
	Lagrangian Interpolation
	Hermite Interpolation
