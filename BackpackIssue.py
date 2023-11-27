import random


def backpack(weight, value, total_weight=25):
    list = []
    for i in range(len(weight)):
        list.append({
            'weight': weight[i],
            'value': value[i],
        })

    print("list: ", list)

    space_left = total_weight
    product_value = 0
    product_list = []
    i = 0

    while i < len(list):
        if list[i]['weight'] <= space_left:
            space_left -= list[i]['weight']
            product_value += list[i]['value']
            product_list.append(list[i])
            print(f"add: {list[i]}, product value: {product_value}, space left: {space_left}")
        i += 1
    return product_value, product_list


weight = []
value = []
for i in range(0, 7):
    weight.append(random.randint(1, 25))
    value.append(random.randint(1, 100))
    print(f"weight: {weight}, value: {value}")

print(backpack(weight, value))
