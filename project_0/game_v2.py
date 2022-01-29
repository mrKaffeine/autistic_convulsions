import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        top_limit: Верхняя граница рандомайзера предполагаемого числа
        bottom_limit: Нижняя граница рандомайзера предполагаемого числа
        number (int, optional): Загаданное число. Defaults to 1.
        
    top_limit и bottom_limit введены для сужения области поиска правильного числа.
    
    Returns:
        count: Число попыток
    """
    
    count = 0
    bottom_limit = 1
    top_limit = 101
    
    while True:
        count += 1        
        predict_number = np.random.randint(bottom_limit, top_limit) # предполагаемое число
        
        if number == predict_number: 
            break
        elif predict_number < number: 
            bottom_limit = predict_number
        else:
            top_limit = predict_number + 1
        
    return(count)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        score: среднее количество попыток
    """
    
    count_Is = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size = (1000)) # загадали список чисел
    
    for number in random_array:
        count_Is.append(random_predict(number))
    
    score = int(np.mean(count_Is)) # находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')
    return(score)

print(f'Количество попыток: {random_predict()}')
score_game(random_predict)