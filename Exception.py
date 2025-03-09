try:
    # Code that may raise an exception
    x = 1 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Exception caught: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("No exceptions occurred!")
finally:
    print("This block always executes, whether an exception occurs or not.")
