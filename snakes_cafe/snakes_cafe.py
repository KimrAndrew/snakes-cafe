# Width of menu
WIDTH = 38
# Width of border chars
BORDER = 4
# List of Appetizers
APPETIZERS = ['Wings','Cookies','Spring Rolls']
# List of Entrees
ENTREES = ['Salmon','Steak','Meat Tornado', 'A Literal Garden']
# List of Desserts
DESSERTS = ['Ice Cream', 'Cake', 'Pie']
# List of Drinks
DRINKS = ['Coffee', 'Tea', 'Unicorn Tears']
# Full menu
MENU = APPETIZERS + ENTREES + DESSERTS + DRINKS
# Input Icon
PROMPT = '> '

def createBr(char):
    br = char * WIDTH
    return br

def addWhiteSpace(str):
    # add white space to pad given string
    # should be based off of WIDTH constant instead of a magic number
    return f'{{: ^{WIDTH - BORDER}}}'.format(str)

def lineTemplate(str):
    # create line break if given empty string
    # else add padding to given string
    # should this raise an exception if given a string longer than the format width?
    if not len(str) == 0:
        str = addWhiteSpace(str)
    # return str surrounded by **'s
    return f'{{:*^{WIDTH}}}'.format(str)

def printMenuHeader():
    print(lineTemplate(""))
    print(lineTemplate("Welcome to the Snakes Cafe"))
    print(lineTemplate("Please see our menu below."))
    print(lineTemplate(" "))
    print(lineTemplate("To quit at any time, type \"quit\""))
    print(lineTemplate(""))

def printSectionItems(items):
    for i in range(len(items)):
        print(items[i])

def printMenuSection(category, items):
    print('\n')
    print(category)
    print('-' * len(category))
    printSectionItems(items)

def printOrderPrompt():
    print('\n')
    print(lineTemplate(''))
    print(lineTemplate('What would you like to order?'))
    print(lineTemplate(''))

def handleOrder(order,item):
    if not item in MENU:
        print(lineTemplate(f'Sorry, we don\'t carry {item}'))
        return
    if not order.get(item) == None:
        order.update({item: order[item] + 1})
    else:
        order.update({item: 1})
    printOrder(order,item)
    return {item: order[item]}

def printOrder(order,item):
    plural = 'order'
    if order[item] > 1:
        plural += 's'
    formattedOrder = f'{order[item]} {plural} of {item} have been added to your meal'
    print(lineTemplate(formattedOrder))



def getOrders():
    order = {}
    while True:
        item = input(PROMPT)
        if item == 'quit':
            break
        handleOrder(order,item)
    return order

# def getSummary(order):
    

# def printSummary(order):
#     print(lineTemplate(''))
#     print(lineTemplate('Summary'))

#     for item in order:


#     print(lineTemplate(''))

printMenuHeader()
printMenuSection('Appetizers', APPETIZERS)
printMenuSection('Entrees', ENTREES)
printMenuSection('Desserts', DESSERTS)
printMenuSection('Drinks', DRINKS)
printOrderPrompt()
print(getOrders())

