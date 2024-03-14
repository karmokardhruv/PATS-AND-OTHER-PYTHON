string = 'program_tutorial'
print('Snake case:',string)
result = string.replace('_',' ').title()
result = result.replace(' ','')
print('Pascal case:',result)