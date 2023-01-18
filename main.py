# main document of program


# Функция проверки корректности ввода слов
def exam_cipher(enter, choice):
    if enter not in choice:
        return True
    else:
        return False

# Функция шифрования пользовательского текста
def cipher_func(language, step_decipher, text):
    if language == 'рус':

print('Добро пожаловать в программу шифрования различных текстов с помощью шифра Цезаря!')

print('Вы хотите зашифровать или расшифровать сообщение?')
cipher = input()
choice_cipher = 'зашифроватьрасшифровать'
while exam_cipher(cipher, choice_cipher):
    print('Введите слово "зашифровать" или слово "расшифровать"')
    cipher = input()

print('Какой язык вы хотите использовать? (Русский - "рус", Английский - "англ"')
language = input()
choice_language = 'русангл'
while exam_cipher(language, choice_language):
    print('Введите "рус" если текст на русском языке или "англ" если текст на английском')
    language = input()

if language == 'рус' and cipher == 'зашифровать':
    print('Введите шаг шифрования от 1 до 32')
    step_cipher = int(input())
    print('Введите текст который хотите зашифровать:')
    text_cipher = input()
elif language == 'рус' and cipher == 'расшифровать':
    print('Введите шаг расшифровки от 1 до 32')
    step_decipher = int(input())
    print('Введите текст который хотите расшифровать:')
    text_cipher = input()
elif language == 'англ' and cipher == 'зашифровать':
    print('Введите шаг шифрования от 1 до 25')
    step_cipher = int(input())
    print('Введите текст который хотите зашифровать:')
    text_cipher = input()
elif language == 'англ' and cipher == 'расшифровать':
    print('Введите шаг расшифровки от 1 до 25')
    step_decipher = int(input())
    print('Введите текст который хотите расшифровать:')
    text_cipher = input()


