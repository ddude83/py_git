class Calculator:

  def __init__(self):
    pass

  def add(self, num1, num2):
    return num1 + num2

  def subtract(self, num1, num2):
    return num1 - num2

  def multiply(self, num1, num2):
    return num1 * num2

  def divide(self, num1, num2):
    if num2 == 0:
      return "Error: Cannot divide by zero"
    return num1 / num2

  def run(self):
    while True:
      # Get user input for operation
      print("Choose operation:")
      print("1. Add")
      print("2. Subtract")
      print("3. Multiply")
      print("4. Divide")
      print("5. Exit")

      choice = input("Enter choice(1/2/3/4/5): ")

      # Get numbers
      if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
      
      # Perform operation based on user choice
      result = None
      if choice == '1':
        result = self.add(num1, num2)
      elif choice == '2':
        result = self.subtract(num1, num2)
      elif choice == '3':
        result = self.multiply(num1, num2)
      elif choice == '4':
        result = self.divide(num1, num2)
      elif choice == '5':
        print("Exiting calculator...")
        break
      else:
        print("Invalid Input")

      # Print result if valid operation
      if result is not None:
        print(num1, choice, num2, "=", result)  

# Create a calculator object and run it
calculator = Calculator()
calculator.run()