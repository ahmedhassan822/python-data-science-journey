# A good practice to set manually 'datatype' to improve ptofrence and
# make program more efficient
# diffrent data types are as fallow
# integer data type (int8, int16 , int32,int64)
# float data type (float8, float16, float32)
# boolean data type (bool_)
# string data type (str_,<u#)
# object data type(object_)
import numpy as np
# for int8
arr1=np.array([1,2,3,4,5],dtype=np.int8)
print(arr1.dtype)
print(f"array used {arr1.nbytes} bytes")

# for int 16
arr2=np.array([1,2,3,4,5],dtype=np.int16)
print(arr2.dtype)
print(f"array used {arr2.nbytes} bytes")

#for int32
arr3=np.array([1,2,3,4,5],dtype=np.int32)
print(arr3.dtype)
print(f"array used {arr3.nbytes} bytes")

# for int64
arr4=np.array([1,2,3,4,5],dtype=np.int64)
print(arr4.dtype)
print(f"array used {arr4.nbytes} bytes")

# now we chaeck the range of integer data type
arr5=np.array([123,124,127,128],dtype=np.int16)
print(arr5.dtype)
print(f"array used {arr5.nbytes} bytes")
print(arr5)
# If use the int 8 for above the value of 127 than an error "Python integer 128 out of bounds for int8"

# float data type
arr6=np.array([123,124,127,128],dtype=np.float32)
print(arr6.dtype)
print(f"array used {arr5.nbytes} bytes")
print(arr6)

# boolean data type
arr7=np.array([0,123,124,127,128],dtype=np.bool_)
print(arr7.dtype)
print(f"array used {arr5.nbytes} bytes")
print(arr7)
# in boolean 0='false' and 1='true'

# boolean data type
arr8=np.array([0,123,124,127,128],dtype=np.str_)
print(arr8.dtype)
print(f"array used {arr5.nbytes} bytes")
print(arr8)

# object data type
arr9=np.array([0,'ahmed hussain','abc','true',12.8],dtype=np.object_)
print(arr9.dtype)
print(f"array used {arr5.nbytes} bytes")
print(arr9)
# object is used for when diffrent data type used in one arry
