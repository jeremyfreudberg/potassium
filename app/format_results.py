def nice(s, element):
    data = s.split('|')
    result = '{} in {} of {}:'.format(element, data[2], data[0][8:])
    return result
