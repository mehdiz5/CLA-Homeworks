import numpy as np 


def convert_to_floats(rows):
   result = [] #creating an empty list to stock the converted values
   for row in rows: #looping in the rows
      value = np.asarray(row)
      value = value.astype(np.float)
      result.append(value)  # Vstack means we are adding a row

   return np.array(result) #return a numpy array containing the converted rows


