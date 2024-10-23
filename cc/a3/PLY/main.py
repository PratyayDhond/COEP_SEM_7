from parser import parser

# Main loop for user input
def main():
    print("Scientific Calculator. Type 'exit' or 'quit' to end.")
    while True:
        try:
            s = input('calc > ')
            if s.lower() in ['exit', 'quit']:
                break
        except EOFError:
            break
        if not s:
            continue
        try:
            result = parser.parse(s)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()

