def main():
    answer = input("Enter a file with extension: ")
    match answer.lower().strip():
        case answer if answer.endswith(".gif"):
            print("image/gif")
        case answer if answer.endswith((".jpg",".jpeg")):
            print("image/jpeg")
        case answer if answer.endswith(".png"):
            print("image/png")
        case answer if answer.endswith(".pdf"):
            print("application/pdf")
        case answer if answer.endswith(".txt"):
            print("text/plain")
        case answer if answer.endswith(".zip"):
            print("application/zip")
        case _:
            print("application/octet-stream")

main()