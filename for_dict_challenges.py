# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
print('Задание 1')
import collections
from collections import Counter

students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
all_names = []
for name in students:
    all_names.append(name['first_name'])
    #print(', '.join(all_names))
count = Counter(all_names)
for nn in count:
  print(f'{nn}:', count[nn])


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
  {'first_name': 'Оля'},
  {'first_name': 'Оля'},
  {'first_name': 'Оля'},
]
one_list = []
for person in students:
  one_list.append(person['first_name'])

most_common = None
qty_most_common = 0

for name in one_list:
    qty = one_list.count(name)
    #print(qty)
    if qty > qty_most_common:
        qty_most_common = qty
        most_common = name
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
    {'first_name': 'Сеня'},
    {'first_name': 'Саня'},
  ]
]
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша
one_class = []
n = 0
for one_class in school_students:
  n += 1
  #print(f'класс номер {n}', one_class)
  klass = []
  for names in one_class:
    klass.append(names['first_name'])
    #print(f'имена класса {n}', ', '.join(klass))

  most_common = None
  qty_most_common = 0

  for person in klass:
    #print(f'имя ученика класса {n}:', person)
    qty = klass.count(person)
    #print(f'число {person} в классе {n}', qty)
    if qty > qty_most_common:
        qty_most_common = qty
        most_common = person
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

one_class = []
for klass in school:
  one_class = klass['students']
  #print(one_class)
  persons = []
  m = 0
  f = 0
  for name in one_class:
    persons = name['first_name']
    #print(persons)
    if is_male[persons] == True:
      #print(f'{persons} - мальчик')
      m += 1
    else:
      #print(f'{persons} - девочка')
      f += 1
  print(f'В классе {klass["class"]} {f} девочки и {m} мальчика')

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
pupils = []
boys = 0
girls = 0
male_klass = None
fem_klass = None
for klass in school:
  pupils = klass['students']
  #print(pupils)
  names = []
  m = 0
  f = 0
  for person in pupils:
    names = person['first_name']
    #print(person)
    #print(names)
    if is_male[names] == True:
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