#импорт нужных модулей
import numpy as cp
import argparse

#функция преобразования текста в вектор cupy, который хранится на GPU
def text_to_vector(text):
    out = []
    for i in range(len(text)):
        out.append(ord(text[i]) - 65)
    return cp.asarray(out)

#Функция преобразования векторов в текст и его вывода
def print_text_from_array(text_array, text):
    for i in range(len(text)):
        if ('A' <= text[i] <= 'Z'):
            print(chr(text_array[i] + 65), end='')
        else:
            print(text[i], end='')
    print()
    return
#добавляем парсер аргументов для интерфейса командной строки
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-t', '--text', type=str, dest='text', help='Enter the text to encode/decode')
parser.add_argument('-s','--stride',  dest='stride', help='Enter the key to encode text or leave empty to brutefoce')
args=parser.parse_args()
text=args.text
stride=args.stride
decrypt_mode = stride==None
text_array=text_to_vector(text)

#часть для брутфорса и вывод списка результатов
if decrypt_mode:
  print("### Starting decrypt mode. Prepare your GPU's) ###")
  matrix = cp.asarray([text_array for _ in range(27)])
  for i in range(27):
    matrix[i]=(matrix[i]+i)%26
  for i in matrix:
    print_text_from_array(i, text)
#часть шифрования, где прибавляется сдвиг и выводится результат
else:
  print("Your encrypted text: ", end='')
  stride=int(stride)
  text_array=(text_array+stride)%26
  print_text_from_array(text_array, text)


