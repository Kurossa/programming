#Create proper python file with main function.

#Create main function that will ask for two numbers, and it will say which is bigger. Create function for checkin those vairables. If it will be not too hard. Put one variable as global and put any value you want.
#Program can ask in loop all time "Gess number, enter your guese:" till user will find out what is number you put.

#USE ANY HELP YOU WANT (INTERNET, BOOKS) BUT PLEASE DO NOT COPY CODE, BUT REWRITE IT BY YOUR SELF LETER BY LETER.

number = 143

def check():
    number_search = input()
    number_search = int(number_search)
    searching_number(number_search)

def searching_number(number_search):
    global number
    if number_search > number:
        print("The number you're looking for is to big. Try again:")
    elif number_search < number:
        print("The number you're looking for is to small. Try again:")
    else:
        print("Yes! This is the number!")
        return (number)
    check()

def main():
    check()

if __name__ == "__main__":
    main()