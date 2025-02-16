number = 17; 
given_number = int(input('enter any number: '))

if given_number > number: 
    answer = (abs(given_number - number)) * 2
    print(f'double absolute difference is {answer}')
else: 
    print(f'answer is {given_number - number}') ; 

