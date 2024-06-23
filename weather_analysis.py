#Student Name: Sudhir Paudel(Student ID: c0938269)
#Assignment: 5 (Weather Analysis)

# Defining the temperature data
temperatures = [19, 28, 16, 21, 29, 14, 26, 18, 19, 22, 27, 21, 23, 17, 16, 18, 19, 21, 24, 26, 25, 22, 21, 20, 19, 18, 17, 15, 14, 13]

def calculate_average(temp_list):
    """
    Calculates the average temperature from the given list of temperatures.
    
    Args:
        temp_list (list): A list of temperature values.
    
    Returns:
        float: The average temperature.
    """
    if not temp_list:
        return 0.0
    
    total = sum(temp_list)
    average = total / len(temp_list)
    return average

def find_max_temp(temp_list):
    """
    Finds the maximum temperature from the given list of temperatures.
    
    Args:
        temp_list (list): A list of temperature values.
    
    Returns:
        int: The maximum temperature.
    """
    if not temp_list:
        return 0
    
    return max(temp_list)

def find_min_temp(temp_list):
    """
    Finds the minimum temperature from the given list of temperatures.
    
    Args:
        temp_list (list): A list of temperature values.
    
    Returns:
        int: The minimum temperature.
    """
    if not temp_list:
        return 0
    
    return min(temp_list)

def count_temps(temp_list):
    """
    Counts the frequency of each temperature in the given list of temperatures.
    
    Args:
        temp_list (list): A list of temperature values.
    
    Returns:
        dict: A dictionary where the keys are temperatures and the values are their respective counts.
    """
    temp_freq = {}
    for temp in temp_list:
        if temp in temp_freq:
            temp_freq[temp] += 1
        else:
            temp_freq[temp] = 1
    return temp_freq

# Calculating and displaying the results
avg_temp = calculate_average(temperatures)
max_temp = find_max_temp(temperatures)
min_temp = find_min_temp(temperatures)
temp_frequency = count_temps(temperatures)

print(f"Average Temperature: {avg_temp:.1f}°C")
print(f"Maximum Temperature: {max_temp}°C")
print(f"Minimum Temperature: {min_temp}°C")
print("Temperature Frequency:", temp_frequency)