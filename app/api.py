import wolframalpha
from .constants import APP_KEY
c = wolframalpha.Client(APP_KEY)

def process(element, food, amount, unit):
    query = '{} in {} {} of {} to milligrams'.format(element, amount, unit, food)
    r = c.query(query)
    data = []
    for pod in r.pods:
        data.append(pod)
    return data[0].text, data[1].text
