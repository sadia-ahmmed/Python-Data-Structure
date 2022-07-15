# Efficient for large sequence of number >10k
# takes less memory
# performs  a little bit faster
# only if there is performance problems when list is used
"""
Type Code	C++ Type	Python Type	Minimum Sizes in Bytes
‘c’	        char	    character	1
‘b’	        signed char	    int`	1
‘B’	        unsigned char	int	1
‘u’	        Py_UNICODE	unicode character	2
‘h’	        signed short	int	2
‘H’	        unsigned short	int	2
‘i’	        signed int	int	2
‘I’	        unsigned int	long	2
‘l’	        signed long	int	4
‘L’     	unsigned long	long	4
‘f’	        float	float	4
‘d’	        double	float	8
"""
from array import array

# module array -> class array

nummber_arr = array("i", [1, 2, 3])  # typecode required
nummber_arr.insert(4)
nummber_arr.pop()
# other data type not allowed
