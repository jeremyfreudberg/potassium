def nice(s, element):
    """ Simplify Wolfram Alpha output, for better UX """
    data = s.split('|')
    result = '{} in {} of {}:'.format(element, data[2], data[0][8:])
    return result
