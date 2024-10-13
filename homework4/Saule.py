import random

def find_multiples_of_x():
    numbers = [random.randint(0, 200) for _ in range(10)]
    print(f"Сгенерированные числа: {numbers}")
    
    while True:
        try:
            x = int(input("Введите цифру X для поиска кратных чисел: "))
            if x == 0:
                print("Цифра X не может быть равна нулю. Пожалуйста, введите другое число.")
                continue
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")
    multiples = list(filter(lambda num: num % x == 0, numbers))
    
    print(f"Числа, кратные {x}: {multiples}")

if __name__ == "__main__":
    find_multiples_of_x()
