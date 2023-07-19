import random #dzieki tej bibliotece mozemy losowo pobierac liczby

computer_digit = random.randrange(0, 10) #pobieramy liczby z zakresu od 1 do 9
print("Computer has chosen a number between 0 and 9. Try to guess the number")

def gueesing(user_digit):
    if computer_digit > 5:
        print('Correct')
        print(computer_digit)
    elif computer_digit < 5:
        print('Incorrect')
        print(computer_digit)
    else:
        print("Ok")
        print(computer_digit)
gueesing(computer_digit)
print('\n' * 2,'*****************', '\n')
print('Another gueesing by Computer')
computer_number = random.randint(0, 5+3) #zaczynamy od 0 do 5+3 czyli do 8, 9 pozostawiona jest dla opcji else
def gueesing_01(computer_number):
    if computer_number > 5:
        print("You get it! ")
        print(computer_number)
    elif computer_number < 5:
        print('You are wrong!')
        print(computer_number)
    else:
        print('Stupid monkey - you are wrong!')
        print(computer_number)
gueesing_01(computer_number)


print('\n' * 3) #tworzymy przerwe na trzy linie 


############### wersja z ograniczeniem wyboru od 0 do 9 przez uzytkownika 
# w przypadku wybrania numeru z poza wraca do prosby o podanie numeru lub w przypadku podania znaku innego niz cyfra wysiwetla komunikat informujacy o tym zajssciu
def user_choice():
    while True:
        try:
            user_digit = int(input('Please enter a number between 0 and 9: '))
            if 0 <= user_digit <= 9:
                return user_digit
            else:
                print('Invalid input. Please enter a number between 0 and 9')
        except ValueError:
            print('Invalid input. Please enter a valid number.')

user_digit = user_choice()
print(user_digit)

def gueesing_02(user_digit):
    if user_digit > 5:
        print("You get it! The number is greater than 5.")
    elif user_digit < 5:
        print('You are wrong! The number is less than 5.')
    else:
        print('Stupid monkey. The number is exactly 5.')

gueesing_02(user_digit)

