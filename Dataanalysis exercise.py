#import numpy library
import numpy as np



#creating an empty list variable
My_list = []

#creating an entry method
def Method_entry():
    
    #creating the user entry for numbers

    i=0
    while(i<9):
        try:
            User_numbers = int(input("\n enter numbers only: "))#converts user input to integer
            i+=1
            My_list.append(User_numbers)
            print(My_list)
        except ValueError:
            print("invalid input")
        

#creating the calculate function

def Calculate(My_list):
    
    #converting the list to nparray
    Toarray = np.array(My_list)
    Matrix_size = np.reshape(Toarray,(3,3))#converting nparray to 3x3 matrix
    print(Matrix_size)

    #calculating the mean of the matrix
    Mean_axis1 = Matrix_size.mean(axis=1)
    Mean_axis2 = Matrix_size.mean(axis=-1)
    Mean_flattened = Toarray.mean()

    #calculating the variance of the matrix
    Variance_axis1 = Matrix_size.var(axis=1)
    Variance_axis2 = Matrix_size.var(axis=-1)
    Variance_flattened = Toarray.var()

    #calculating the standard deviation of the matrix
    STD_axis1 = Matrix_size.std(axis=1)
    STD_axis2 = Matrix_size.std(axis=-1)
    STD_flattened = Toarray.std()

    #calculating the max of the matrix
    Max_axis1 = Matrix_size.max(axis=1)
    Max_axis2 = Matrix_size.max(axis=-1)
    Max_flattened = Toarray.max()

    #calculating the min of the matrix
    Min_axis1 = Matrix_size.min(axis=1)
    Min_axis2 = Matrix_size.min(axis=-1)
    Min_flattened = Toarray.min()

    #calculating the sum of the matrix
    
    Sum_axis1 = Matrix_size.sum(axis=1)
    Sum_axis2 = Matrix_size.sum(axis=-1)
    Sum_flattened = Toarray.sum()

    #cpnverting the output of the fuction to a dictionary
    My_output = {"mean":[Mean_axis1, Mean_axis2, Mean_flattened],
                 "variance":[Variance_axis1, Variance_axis2, Variance_flattened],
                 "standard deviation":[STD_axis1, STD_axis2, STD_flattened],
                 "max":[Max_axis1, Max_axis2, Max_flattened],
                 "min":[Min_axis1, Min_axis2, Min_flattened],
                 "sum":[Sum_axis1, Sum_axis2, Sum_flattened]}
    print(My_output)


    
#calling my main method
    
Method_entry()

#calling calculate fxn
Calculate(My_list)

