import sys, convert
from types import NoneType

sum=float(0)
for i in range(1,len(sys.argv)):
    if type(convert.str_to_float(sys.argv[i]))!= NoneType:
        sum=sum+convert.str_to_float(sys.argv[i])


if __name__ == '__main__':
    print(sys.argv)
    print(sum)