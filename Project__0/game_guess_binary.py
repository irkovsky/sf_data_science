import numpy as np
from game_guess_number import average_result

number = np.random.randint(1,101)
print('number', number)


def guess_number(number:int=1) -> int:
    start = 1
    end = 101
    count = 1
    
    while True:
        middle = start + int((end-start)/2)
        
        if number == middle: break
        
        if number > middle: start = middle + 1
        elif number < middle: end = middle - 1
        
        # print(count, 'middle=', middle, 'start=', start, 'end=', end)
        count += 1
        
    return count


print('number of guesses =', guess_number(number))
print('average result =', average_result(guess_number))

    
    
    
        