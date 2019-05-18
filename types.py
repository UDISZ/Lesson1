v = input("Введите число от 1 до 10: ")
m = int(v)
d = m+10
print(d)

name = input('Введите ваше имя: ')

print(f"Привет! {name}! Как дела?")

numbers = [3, 5, 7, 9, 10.5]
print(numbers)
numbers.append("Python")
print(numbers)
print(len(numbers))
print(numbers[0])
print(numbers[5])
del numbers[5]
print(numbers)
weather = {"city": "Москва", "temperature": 20}
print(weather.get("city"))
weather["temperature"] -=5
print(weather)
print(weather.get("country", "Russia"))
weather = {"city": "Москва", "temperature": 20, 'date': '27.05.2019'}
print("Длинна словаря:")
print(len(weather)) 