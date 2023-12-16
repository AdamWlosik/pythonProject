import random
import pdb
import matplotlib.pyplot as plt

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
    return [[(random.choice([True, False])) for _ in range(len(ITEMS))] for _ in range(0, 300)]


# print(first_generation())

def iterate_for_fitness(generation):
    generation_after_fitness = []
    for individual in generation:
        generation_after_fitness.append([individual, fitness(individual)])
    return generation_after_fitness


def fitness(individual):
    # breakpoint()
    individual_fitness = 0
    individual_weight = 0
    for index, i in enumerate(individual):
        if i == 0:
            continue
        # print("ITEMS:", ITEMS[index][1])
        individual_fitness += ITEMS[index][0]
        individual_weight += ITEMS[index][1]
        if individual_weight > 25:
            return 0

    return individual_fitness


def selection(generation_after_fitness):
    generation_after_fitness.sort(key=lambda individual: individual[1])
    top50 = generation_after_fitness[:50]
    return top50


def iterate_for_crossover(top50):
    after_cressover = []
    for i in range(150):
        candidate1, candidate2 = random.sample(top50, k=2)
        after_cressover.extend(crossover(candidate1[0], candidate2[0]))
        return after_cressover


def crossover(first, second):
    first_part = first[:5]
    second_part = second[5:]
    child1 = first_part + second_part
    child2 = second_part + first_part
    return child1, child2


def iterate_for_mutation(next_generation, mut_rate):
    for i in next_generation:
        if random.random() < mut_rate:
            # breakpoint()
            mutation(i)


def mutation(mut):
    pos = random.randint(0, len(mut) - 1)
    mut[pos] = not mut[pos]


def calculate_statistic(iterate_for_fit):
    # breakpoint()
    fitnesses = [item[1] for item in iterate_for_fit]
    maxf = max(fitnesses)
    minf = min(fitnesses)
    avgf = sum(fitnesses) / len(fitnesses)
    print(maxf, minf, avgf)
    return maxf, minf, avgf


def diagram(max_fitness_value, min_fitness_value, avg_fitness_value):
    generations = list(range(1, 1001))
    plt.plot(generations, max_fitness_value, label='MAX Fitness')
    plt.plot(generations, min_fitness_value, label='MIN Fitness')
    plt.plot(generations, avg_fitness_value, label='AVG Fitness')

    plt.xlabel('Generations')
    plt.ylabel('Fitness')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    generation = first_generation()
    x = 0
    # statistics = []
    max_fitness_values = []
    min_fitness_values = []
    avg_fitness_value = []
    while x < 1000:
        iterate_for_fit = iterate_for_fitness(generation)
        # statistics.append(calculate_statistic(iterate_for_fit))
        max_fitness, min_fitness, avg_fitness = (calculate_statistic(iterate_for_fit))
        max_fitness_values.append(max_fitness)
        min_fitness_values.append(min_fitness)
        avg_fitness_value.append(avg_fitness)
        selected = selection(iterate_for_fit)
        next_generation = iterate_for_crossover(selected)
        iterate_for_mutation(next_generation, 0.083)
        x += 1
        generation = next_generation

    diagram(max_fitness_values, min_fitness_values, avg_fitness_value)

# dopisać zwracanie uwagi na wage 25kg if waga > 25 individual_fitness = 0
# selekcja 50 z najlepszą fintess
# krzyzowanie zeby było znowu 300
# prawdopodobieństow mutaci 8,3%
# zbierać max min avg


# przerobić żeby zrobił ryunek mat pro lib
