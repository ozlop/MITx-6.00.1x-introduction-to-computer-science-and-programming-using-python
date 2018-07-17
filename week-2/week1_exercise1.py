x = 36
low = 0
high = 100
ans = (high + low)/2

while True:
    print('Is your secret number ' + str(int(ans)) + '?')
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if response == 'c':
        print('Game over. Your secret number was: ' + str(int(ans)))
        break
    
    elif response == 'l':
        low = ans
    
    elif response == 'h':
        high = ans
    
    else:
        print("Sorry, I did not understand your input.")
    
    ans = (high + low)/2
