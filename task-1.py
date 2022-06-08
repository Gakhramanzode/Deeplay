import re

# путь или название файла
file = "/content/drive/MyDrive/log.txt"

# получим объект файла
with open(file, "r", encoding='utf-8') as log:
    # считываем все строки
    lines = log.readlines()

# создаем массив, в который будем складывать все нужные нам значения sid
array = []

# задаем искомый IP (можно сделать интерактивным, чтобы пользователь сам вводил и повесить валидацию)
IP = "10.1.192.38"

# итерация по строкам
for line in lines:
    # ищем нужный IP
    if IP in line:
        regs = re.search('sid\=.*&type\=', line).regs[0]
        array.append(line[regs[0] + 5:regs[1] - 7])

for x in array:
    print(x)
