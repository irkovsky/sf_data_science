''' Guess the number game. Computer takes a number and guesses it itself within 20 tries'''

import numpy as np

def take_number() -> int:
    ''' Computer gives a random integer number.
    
    Returns: random integer number.
    '''
    number = np.random.randint(1, 101) 
    return number    

    
number = take_number()
print(f'Компьютер загадал число {number}')


def start_guess_counter(number:int) -> int: 
    ''' Method of guessing a number. 
    First it sets counter of guesses to zero and returns "guess_number" function.
    
    Args
        number(int): the number computer should guess.
    
    Returns: function which makes guesses and counts tries itself.
    '''
    count = 0
    

    def guess_number(number:int=1, start:int=1, end:int=101)-> int:
        ''' Method of guessing itself.
        Computer makes guesses and counts tries until it's succesful.
        
        Args:
            number(int): the number computer should guess,
            start: min number of the random range for guessing,
            end: max number of the random range for guessing,
        
        Returns:
            count(int, nonlocal): counter for number of guesses.
        '''
        guess_try = np.random.randint(start, end) 
        
        nonlocal count
        count += 1 
        
        if guess_try == number: return count 
        
        if guess_try > number: end = guess_try        
        elif guess_try < number: start = guess_try
            
        return guess_number(number, start, end)
    
    
    return guess_number(number)


guess_number = start_guess_counter           
print(f'Компьютер угадал число {number} за {guess_number(number)} попыток')


def average_result(guess_number) -> int:
    ''' Determines an average number of tries the method needs to guess the number.
    Uses the array of 1000 numbers passed to the method.
    
    Args:
        guess_number: name of guessing method.
    
    Returns:
        int: average number of guesses.
    '''
    
    guesses_array = list(np.random.randint(1, 101, size=1000))
    results = list(map(guess_number, guesses_array))
    return int(np.mean(results))


print(f'Алгоритм угадывает число в среднем за {average_result(guess_number)} попыток')
