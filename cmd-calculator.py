def calculator():
    while True:
        try:
            term = input("Enter a math term (or 'exit' to exit): ")
            if term.lower() == 'exit':
                break
            result = eval(term)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator()