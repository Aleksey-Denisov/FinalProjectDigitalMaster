#Программа должна из имеющегося массива строк формировать массив из строк, длина которых меньше либо равна 3 символа
def fetchArray():
    arrayString = []
    finalArray = []
    lenghtArray = enterLenghtArray("Введите длину массива: ")
    for i in range(lenghtArray):
        arrayString.append(enterUserData(f"Введите значение в элемент массива {i}: "))
        if len(arrayString[i]) <= 3:
            finalArray.append(arrayString[i])
    print(finalArray)

def enterUserData(message):
    userData = input(message)
    return userData

def enterLenghtArray(message):
    while True:
        try:
            lenghtArray = int(input(message))
            break
        except ValueError:
            print("Вы ввели не число! Попробуйте ещё раз")
    return lenghtArray

fetchArray()
