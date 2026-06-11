import random

def generate_random_numbers(n, lower_bound, upper_bound):
    """Gera uma lista de n números aleatórios entre lower_bound e upper_bound."""
    return [random.randint(lower_bound, upper_bound) for _ in range(n)]
# Exemplo de uso
random_numbers = generate_random_numbers(10, 1, 100)
print(random_numbers)
