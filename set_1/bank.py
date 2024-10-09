def main():
    greeting = input("Greeting: ")

    if greeting.lower().lstrip().startswith("hello"):
        print("$0")
    elif greeting.lower().lstrip().startswith("h"):
        print("$20")
    else:
        print("$100")

main()