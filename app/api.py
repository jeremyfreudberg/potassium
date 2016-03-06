import wolframalpha
from .constants import APP_KEY
c = wolframalpha.Client(APP_KEY)

def process(food, amount, unit):
    query1 = 'potassium in {} {} of {} to milligrams'.format(amount, unit, food)
    query2 = 'sodium in {} {} of {} to milligrams'.format(amount, unit, food)
    return lookup(query1), lookup(query2)

def lookup(query):
    r = c.query(query)
    data = []
    for pod in r.pods:
        data.append(pod)
    return data[0].text, data[1].text
