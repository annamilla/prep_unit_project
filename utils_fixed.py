import numpy as np

def convert_to_floats(rows):
    """Convert a list of string tuples to a ndarray of floats."""
    # Create a result list (later to be converted to np array matrix)
    print("convert_to_floats function called")  # Debugging print statement
    result = []
    # To-Do Loop through the list and convert row by row
    # Loop through the list and convert row by row
    for row in rows:
        value = np.asarray(row)
        value = value.astype(np.float64)

        result.append(value)  # vstack means we are adding a row

    return np.array(result)