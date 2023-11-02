def read_cookbook(filename='recipes.txt'):
    cook_book = {}
    with open(filename, encoding='UTF-8') as f1:
        for line in f1:
            name = line.rstrip()
            quantity = int(f1.readline())
            ingredient_list = []
            for x in range(quantity):
                ingredient_name, quantity, measure = f1.readline().split(" | ")
                ingredient_list.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': str(measure).rstrip()
                })
            f1.readline()
            cook_book[name] = ingredient_list
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    ingredient_dict = {}
    cook_book = read_cookbook()
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                title = ingredient['ingredient_name']
                if title not in ingredient_dict:
                    ingredient_dict[title] = {
                        'measure': ingredient['measure'],
                        'quantity': ingredient['quantity'] * person_count
                    }
                else:
                    ingredient_dict[title]['quantity'] += ingredient['quantity'] * person_count
    return ingredient_dict


print(read_cookbook())
print(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 3))
