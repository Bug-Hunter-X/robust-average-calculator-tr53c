def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 # Handle list with no numeric values
    return sum(numeric_numbers) / len(numeric_numbers)

# Example usage
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = []
average = calculate_average(my_numbers) 
print(f"The average is: {average}")

my_numbers = [10, 20, 'a']
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = ['a', 'b', 'c']
average = calculate_average(my_numbers)
print(f"The average is: {average}") 