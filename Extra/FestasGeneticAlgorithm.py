import random

# Define the target phrase we want to evolve
TARGET_PHRASE = "Hello, my name is Festa!"

# Define possible genes (characters) that can be used in the population
GENES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ! ,."

# Set the population size and mutation rate
POPULATION_SIZE = 200
MUTATION_RATE = 0.01

# Function to create an initial population
def create_population():
    return [''.join(random.choice(GENES) for _ in range(len(TARGET_PHRASE))) for _ in range(POPULATION_SIZE)]

# Function to calculate the fitness of an individual
#counts the number of matching characters by summing up 1 for each matching pair of characters
def calculate_fitness(individual):
    return sum(1 for expected, actual in zip(TARGET_PHRASE, individual) if expected == actual)

# Function for selection using roulette wheel selection ("fitness proportionate selection)
#selects top2 based on fitnes scores
def selection(population, fitness_scores):
    return random.choices(population, weights=fitness_scores, k=2)

# Function for crossover (single-point crossover)
def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Function for mutation
def mutate(individual):
    mutated_individual = list(individual)
    for i in range(len(mutated_individual)):
        if random.random() < MUTATION_RATE:
            mutated_individual[i] = random.choice(GENES)
    return ''.join(mutated_individual)

# Main genetic algorithm function
def genetic_algorithm():
    population = create_population()

    generation = 1
    while True:
        fitness_scores = [calculate_fitness(individual) for individual in population]

        # Check for the best individual in the population
        best_individual = population[fitness_scores.index(max(fitness_scores))]
        print(f"Generation {generation}: {best_individual}")

        # If target phrase found, break the loop
        if best_individual == TARGET_PHRASE:
            break

        # Perform selection, crossover, and mutation to create a new generation
        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent1, parent2 = selection(population, fitness_scores)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1), mutate(child2)])

        population = new_population
        generation += 1

# Run the genetic algorithm
genetic_algorithm()
