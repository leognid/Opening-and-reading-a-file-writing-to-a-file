def dict_collector(file_path):
    with open(file_path, 'r',encoding = 'utf 8' ) as file_work:
        menu = {}
        for line in file_work:
            dish_name = line[:-1]
            counter = file_work.readline().strip()
            list_of_ingridient = []
            for dish in range(int(counter)):
                dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])
                ingridient = file_work.readline().strip().split(' | ') 
                for item in ingridient:
                    dish_items['ingredient_name'] = ingridient[0]
                    dish_items['quantity'] = ingridient[1]
                    dish_items['measure'] = ingridient[2]
                list_of_ingridient.append(dish_items)
                cook_book = {dish_name: list_of_ingridient}
                menu.update(cook_book)
            file_work.readline()

    return(menu)

dict_collector('recipe.txt')
def get_shop_list_by_dishes(dishes, persons=int):
    menu = dict_collector('recipe.txt')
    print('Ознакомьтесь с меню :')
    print(menu)
    print()
    shopping_list = {}
    try:
        for dish in dishes:
            for item in (menu[dish]):
                items_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity'])*persons})])
                if shopping_list.get(item['ingredient_name']):
                    extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) +
                                  int(items_list[item['ingredient_name']]['quantity']))
                    shopping_list[item['ingredient_name']]['quantity'] = extra_item
                else:
                    shopping_list.update(items_list)
        print(f'Для приготовления блюд на {persons} человек  нам необходимо купить:')
        print(shopping_list)
    except KeyError:
         print('Ошибка в названии блюда')
get_shop_list_by_dishes(['Запеченный картофель', 'Фахитос'], 2)

def sorted_files(files: list, result_path: str):
    temp_dict = {sum(1 for text in open(one_file, encoding = 'utf-8')): one_file for one_file in files}
    with open(result_path, 'w') as file_write:
      file_write.write('')
    with open(result_path, 'a') as file_write:
      for key in sorted(temp_dict.keys()):
          file_write.write(temp_dict[key] + '\n')
          file_write.write(str(key) + '\n')
          file_write.writelines(line for line in open(temp_dict[key], 'r', encoding = 'utf-8'))
          file_write.write('\n')

def main():
    files = ['1.txt', '2.txt', '3.txt']
    sorted_union_files(files, '4.txt')

if __name__ == '__main__':
    main()