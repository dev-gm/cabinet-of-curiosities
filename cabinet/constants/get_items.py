def get_items():
    items = []
    for file in lisdir('../images'):
        filename = splitext(file)[0]
        items.append(filename)
    shuffle(items)
    return items