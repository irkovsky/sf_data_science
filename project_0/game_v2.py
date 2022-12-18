"""Guess the number game.
The computer itself makes a guess and guesses the number
"""
import numpy as np

def random_predict(number:int=1) -> int:
    """ Рандомно угадываем число
    Args:
      number (int, optional): загаданное число. По умолч.1
    Returns:
      int: чило попыток
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break
        
    return count

print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1,101, size=50)
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    
    print(f'Алгоритм угадывает число в среднем за {score} попыток(-ки)')
    return(score)

if __name__ == '_main_':
  score_game(random_predict)

