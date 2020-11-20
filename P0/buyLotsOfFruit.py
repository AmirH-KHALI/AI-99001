fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75,
               'limes': 0.75, 'strawberries': 1.00}

def buyLotsOfFruit(orderList):
    sum = 0
    for x in orderList:
        sum += x[1] * fruitPrices[x[0]]
    return sum

if __name__ == '__main__':
    orderList = [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)]
    print('Cost of', orderList, 'is', buyLotsOfFruit(orderList))
