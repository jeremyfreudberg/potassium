def nice(s, element):
    data = s.split('|')
    element = element[0].upper() + element[1:]
    result = '{} in {} of {}:'.format(element, data[2], data[0][8:])
    return result
