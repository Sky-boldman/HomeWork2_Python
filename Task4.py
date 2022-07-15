#  Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

import time

def random_number():
    random_string = time.time()     #time.time() - время, выраженное в секундах с начала эпохи.
    str_num = str(random_string)
    return str_num[-1]

print(random_number())
    
                         






