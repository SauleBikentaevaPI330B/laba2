def get_number():
    for number in range(30):
        if number % 2 != 0:  
            yield number  


odd_numbers = list(get_number())

if len(odd_numbers) >= 5:
    first_value = odd_numbers[0]
    fifth_value = odd_numbers[4]
    last_value = odd_numbers[-1]

    print(f"Первое нечетное число: {first_value}")
    print(f"Пятое нечетное число: {fifth_value}")
    print(f"Последнее нечетное число: {last_value}")
else:
    print("Недостаточно нечетных чисел в диапазоне.")
