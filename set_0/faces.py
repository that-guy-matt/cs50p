def convert(s):
    s = s.replace(':)', "🙂")
    s = s.replace(':(', "🙁")
    return s;

def main():
    txt = input("Input some text: ")
    print(convert(txt))

main()
