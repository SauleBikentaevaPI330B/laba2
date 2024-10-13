from datetime import datetime

def calculate_age():
    while True:
        try:
            birth_date_str = input("Введите дату рождения (дд/мм/гггг): ")
            
            birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")
           
            today = datetime.today()
            
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            
            return age
        except ValueError:
            print("Некорректный формат даты. Пожалуйста, введите дату в формате дд/мм/гггг.")

if __name__ == "__main__":
    age = calculate_age()
    print(f"Ваш возраст: {age} лет.")
