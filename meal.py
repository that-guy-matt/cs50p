def main():
    time = convert(input("Input a time: "))
    match time:
        case time if (time >= 7.00 and time <= 8.00):
            print("breakfast time")
        case time if (time >= 12.00 and time <= 13.00):
            print("lunch time")
        case time if (time >= 18.00 and time <= 19.00):
            print("dinner time")

def convert(time):
    time = time.split(':')
    time = [int(i) for i in time]
    time = time[0]+time[1]/60

    return time


if __name__ == "__main__":
    main()