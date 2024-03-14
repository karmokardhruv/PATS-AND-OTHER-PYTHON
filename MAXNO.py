import re
string='123abdefg567yuio908'
number = re.findall('\d+', string)
number = map(int, number)
print(max(number))