from main import *



## Feel free to add your own tests here.
def test_multiply():

    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert quadratic_multiply(BinaryNumber(0), BinaryNumber(2)) == 0*2
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(1)) == 2*1
    assert quadratic_multiply(BinaryNumber(-10), BinaryNumber(2)) == -10*2
    assert quadratic_multiply(BinaryNumber(-10), BinaryNumber(-2)) == -10*-2
    assert quadratic_multiply(BinaryNumber(-10), BinaryNumber(0)) == -10*0
    assert quadratic_multiply(BinaryNumber(-10), BinaryNumber(1)) == -10*1
    assert quadratic_multiply(BinaryNumber(-10), BinaryNumber(-1)) == -10*-1
    assert quadratic_multiply(BinaryNumber(4), BinaryNumber(3)) == 4*3
    assert quadratic_multiply(BinaryNumber(6), BinaryNumber(21)) == 6*21
    assert quadratic_multiply(BinaryNumber(15), BinaryNumber(13)) == 15*13



