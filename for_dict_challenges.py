
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
print('Задание 1')
import collections
#from collections import Counter

students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
  {'first_name': 'Петя'},
  {'first_name': 'Петя'},
]
all_names = [name['first_name'] for name in students]
count = collections.Counter(all_names)
for nn in count:
  #print(f'{nn}:', count[nn])
  print(nn, count[nn])


# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.

print('Задание 2')
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Миша'},
]
one_list = [person['first_name'] for person in students]
most_common = None
for name in one_list:
    most_common = max(set(one_list), key=one_list.count)
print('Самое частое имя среди учеников:', most_common)

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.

print('Задание 3')
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ],
  [ # это - третий класс
    {'first_name': 'Сеня'},
    {'first_name': 'Саня'},
    {'first_name': 'Саня'},
  ]
]
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша
n = 0
for one_class in school_students:
  n += 1
  #print(f'класс номер {n}', one_class)
  each_klass = [person['first_name'] for person in one_class]
  #print(each_klass)
  most_common = None
  for person in one_class:
    most_common = max(set(each_klass), key=each_klass.count)
  print(f'Самое частое имя в классе {n}: ', most_common)

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.

print('Задание 4')
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.
#def split_list():
one_class = []
for klass in school:
  one_class = klass['students']
  #return one_class
  #print(one_class)
  persons = []
  b = 0
  g = 0
  for name in one_class:
    persons = name['first_name']
    #print(persons)
    if is_male[persons] == True:
      #print(f'{persons} - мальчик')
      b += 1
    else:
      #print(f'{persons} - девочка')
      g += 1
  print(f'В классе {klass["class"]} {g} девочки и {b} мальчика')

  # Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
print('Задание 5')
school = [
  {'class': '2a', 'students': [{'first_name': 'Миша'}, {'first_name': 'Оля'}, {'first_name': 'Миша'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Маша'}, {'first_name': 'Маша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
one_class = []
boys = 0
girls = 0
male_klass = None
fem_klass = None
for klass in school:
  one_class = klass['students']
  #print(one_class)
  persons = []
  m = 0
  f = 0
  for name in one_class:
    persons = name['first_name']
    if is_male[persons] == True:
      m += 1
    else:
      f += 1
  #print(f'в классе {klass["class"]} {m} мальчика и {f} девочки')
  if m > boys:      
    boys = m
    male_klass = klass["class"]
  if f > girls:
    girls = f
    fem_klass = klass["class"]
print(f'Больше всего мальчиков в классе {male_klass}')
print(f'Больше всего девочек в классе {fem_klass}')