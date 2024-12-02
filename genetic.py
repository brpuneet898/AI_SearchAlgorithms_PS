import random

# The objective function (fitness function)
def fitness_function(x):
    return x ** 2  # Maximizing x^2

# Generate an initial population
def generate_population(pop_size, min_value, max_value):
    population = []
    for _ in range(pop_size):
        # Each individual in the population is represented by a random integer
        individual = random.randint(min_value, max_value)
        population.append(individual)
    return population

# Select two individuals from the population based on their fitness (roulette wheel selection)
def select_parents(population):
    total_fitness = sum(fitness_function(x) for x in population)
    selection_probs = [fitness_function(x) / total_fitness for x in population]

    # Select two individuals using roulette wheel selection
    parents = random.choices(population, weights=selection_probs, k=2)
    return parents

# Perform crossover between two parents to produce a child
def crossover(parent1, parent2):
    # Choose a random crossover point
    crossover_point = random.randint(1, 31)  # We assume 32-bit integers for simplicity
    # Create a child by combining the parents
    child = (parent1 & (0xFFFFFFFF << crossover_point)) | (parent2 & (0xFFFFFFFF >> crossover_point))
    return child

# Perform mutation on an individual
def mutate(individual, mutation_rate, min_value, max_value):
    if random.random() < mutation_rate:
        # Randomly change one bit of the individual (flip a random bit)
        mutation = random.randint(min_value, max_value)
        individual = individual ^ mutation
    return individual

# Main Genetic Algorithm function
def genetic_algorithm(pop_size, min_value, max_value, generations, mutation_rate):
    # Generate initial population
    population = generate_population(pop_size, min_value, max_value)

    for generation in range(generations):
        # Evaluate the fitness of each individual in the population
        population.sort(key=lambda x: fitness_function(x), reverse=True)  # Sort by fitness (descending)

        # Check if the best individual has reached the target (maximum fitness)
        best_individual = population[0]
        best_fitness = fitness_function(best_individual)
        print(f"Generation {generation}: Best Fitness = {best_fitness}, Best Individual = {best_individual}")

        # If we have found the optimal solution, return it
        if best_fitness == fitness_function(max_value):
            break

        # Create a new population using selection, crossover, and mutation
        new_population = []

        # Keep the best individual (elitism)
        new_population.append(population[0])

        # Generate new individuals by selecting parents and performing crossover and mutation
        while len(new_population) < pop_size:
            parent1, parent2 = select_parents(population)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate, min_value, max_value)
            new_population.append(child)

        # Replace the old population with the new one
        population = new_population

    # Return the best solution found
    best_individual = population[0]
    return best_individual, fitness_function(best_individual)

# Parameters
population_size = 10 
min_value = 0        
max_value = 31        
generations = 50      
mutation_rate = 0.1   

# Run the Genetic Algorithm
best_solution, best_fitness = genetic_algorithm(population_size, min_value, max_value, generations, mutation_rate)
print(f"Best Solution: {best_solution}, Fitness: {best_fitness}")
