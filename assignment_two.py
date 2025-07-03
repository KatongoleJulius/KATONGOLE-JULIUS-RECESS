# DIVISION WITH ERROR HANDLING
# Assignment Two: Safe Division Program
# Features:
# 1. Infinite loop until valid numbers are entered
# 2. Handles division by zero
# 3. Handles non-numeric inputs

while True:  # Infinite loop
    try:
        # Get user input
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        # Attempt division
        result = numerator / denominator
        print(f"Result: {numerator} / {denominator} = {result:.2f}")
        break  # Exit loop if successful
        
    except ValueError:
        print(" Error: Please enter numbers only!")
    except ZeroDivisionError:
        print(" Error: Cannot divide by zero!")

print("Division completed successfully!")