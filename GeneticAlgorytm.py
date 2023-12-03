import random

ITEMS = [(20, 2), (70, 5), (100, 12), (200, 18), (300, 8), (120, 10), (80, 6), (50, 3), (250, 20), (30, 7)]

'''def first_generation(items):
    list = []
    list2 = []
    x = 0
    while x < 300:
        for i in range(len(items)):
            list.append(random.choice([True, False]))
            list2.append(list)
        x += 1

    return list2

print(first_generation(ITEMS))'''


def first_generation():
    generation = [[(random.choice([True, False])) for _ in range(len(ITEMS))] for _ in range(0, 300)]
    return generation


print(first_generation())


def fitness(individual):
    individual_fitness = 0
    for index, i in enumerate(individual):
        if i is True:
            individual_fitness += ITEMS[index][1]
        if individual_fitness > 25:
            return 0

    return individual_fitness


def selection(generation):
    x = 300
    while x > 50:
        select_1 = random.sample(generation)
        select_2 = random.sample(generation)
        fitness_1 = fitness(select_1)
        fitness_2 = fitness(select_2)

        if fitness_1 > fitness_2:
            return select_1
        else:
            return select_2
        x -= 1


def crossover():
    pass


def iterate_for_fitness(generation):
    fitness = 0
    for individual in generation:
        fitness(individual)

# dopisać zwracanie uwagi na wage 25kg if waga > 25 individual_fitness = 0
# selekcja 50 z najlepszą fintess
# krzyzowanie zeby było znowu 300
# prawdopodobieństow mutaci 8,3%
# zbierać max min avg
