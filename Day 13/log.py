import logging

# -----------------------------
# Configure Logging (NO TIMESTAMP)
# -----------------------------
logging.basicConfig(
    filename='calculator.log',
    level=logging.DEBUG,
    format='%(levelname)s - %(message)s'   # removed time
)

logging.info("Program Started")

# -----------------------------
# Calculator Function
# -----------------------------
def calculate(a, b, op):
    logging.debug(f"calculate() called with a={a}, b={b}, op='{op}'")

    if op == '+':
        result = a + b
        logging.info(f"ADD: {a} + {b} = {result}")
        return result

    elif op == '-':
        result = a - b
        logging.info(f"SUBTRACT: {a} - {b} = {result}")
        return result

    elif op == '*':
        result = a * b
        logging.info(f"MULTIPLY: {a} * {b} = {result}")
        return result

    elif op == '/':
        try:
            result = a / b
            logging.info(f"DIVIDE: {a} / {b} = {result}")
            return result
        except ZeroDivisionError:
            logging.error("Division by zero attempted!")
            return "Error: Cannot divide by zero"

    else:
        logging.error(f"Invalid operator received: {op}")
        return "Error: Invalid operator"


# -----------------------------
# User Input
# -----------------------------
try:
    a = float(input("Enter first number: "))
    logging.debug(f"User entered first number: {a}")

    b = float(input("Enter second number: "))
    logging.debug(f"User entered second number: {b}")

    op = input("Enter operator (+, -, *, /): ")
    logging.debug(f"User entered operator: {op}")

    result = calculate(a, b, op)
    print("Result:", result)

except ValueError:
    logging.error("User entered invalid numeric value")
    print("Error: Please enter valid numbers.")

finally:
    logging.info("Program Ended")