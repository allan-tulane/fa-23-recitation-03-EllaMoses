"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)

    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
    #base cases, if either x or y <= 1, just return their product
    if ((x.decimal_val <= 1) or (y.decimal_val  <= 1)):
        return BinaryNumber(x.decimal_val*y.decimal_val)
    #recursive case
    else: 
        #obtain xvec and yvec, the binary_vec values of x and y
        xvec = x.binary_vec
        yvec = y.binary_vec
        #pad xvec and yec so they are the same length and update the variables
        xvec = pad(xvec, yvec)[0]
        yvec = pad(xvec, yvec)[1]
        #split xvec and yvec into two halves
        x_left = split_number(xvec)[0]
        x_right = split_number(xvec)[1]
        y_left = split_number(yvec)[0]
        y_right = split_number(yvec)[1]
        """
        return their product using given formula
        The first term can be found by calling _quadratic_multiply on xl and yl, then using bit shift to multiply by 2^n, where n is the length of xvec (or yvec)
        The second term can be found by using _quadratic_multiply on xl yr and xr yl i then add together the decimal values of these fucntions and convert the sum back to a binary number so I can use bit shift on it to shift this value over 2^n/2, where n is the length of xvec (or yvec)
        The third term can be found using _quadratic_multiply on xr and yr
        I then take the decimal value of each term so i can sum them together
        I then return the BinaryNumber of the sum
        """
        return BinaryNumber((bit_shift(_quadratic_multiply(x_left, y_left), len(xvec))).decimal_val + (bit_shift(BinaryNumber((_quadratic_multiply(x_left, y_right)).decimal_val + (_quadratic_multiply(x_right, y_left)).decimal_val), (len(xvec)//2))).decimal_val + ((_quadratic_multiply(x_right, y_right))).decimal_val)
        

  
def test_quadratic_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(x,y)
    return (time.time() - start)*1000

print(test_quadratic_multiply(BinaryNumber(2),BinaryNumber(1),quadratic_multiply))
print(test_quadratic_multiply(BinaryNumber(2),BinaryNumber(10),quadratic_multiply))
print(test_quadratic_multiply(BinaryNumber(2),BinaryNumber(100),quadratic_multiply))
print(test_quadratic_multiply(BinaryNumber(2),BinaryNumber(1000),quadratic_multiply))
print(test_quadratic_multiply(BinaryNumber(2),BinaryNumber(10000),quadratic_multiply))
print(test_quadratic_multiply(BinaryNumber(2),BinaryNumber(100000),quadratic_multiply))


    
    

