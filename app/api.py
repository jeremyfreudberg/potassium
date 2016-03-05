import wolframalpha
c = wolframalpha.Client('9H34J8-W8T863XLVY')

def process(element, food, amount, unit):
    query = '{} {} {} of {} in milligrams'.format(element, amount, unit, food)
    r = c.query(query)
    data = []
    for pod in r.pods:
        data.append(pod)
    return data[0].text, data[1].text
