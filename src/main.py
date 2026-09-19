import os
import math
import random
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# БЛОК 1: Закон великих чисел
# -------------------------------------------------------------

def run_block_1():
    print("=== БЛОК 1: Закон великих чисел (випробування Бернуллі) ===")
    p_theory = 0.5  # Ймовірність теоретичного успіху
    sample_sizes = [10, 100, 1000, 10000, 100000, 1000000]
    frequencies = []
    errors = []
    
    for N in sample_sizes:
        # Симуляція Бернуллі
        successes = sum(1 for _ in range(N) if random.random() < p_theory)
        w = successes / N
        err = abs(w - p_theory)
        frequencies.append(w)
        errors.append(err)
        print(f"N = {N:>7} | W(A) = {w:.6f} | Похибка = {err:.6f}")
        
    # Побудова графіка для Блоку 1
    plt.figure(figsize=(9, 5))
    plt.plot(sample_sizes, frequencies, marker='o', label="Частота W(A)", color='blue')
    plt.axhline(y=p_theory, color='red', linestyle='--', label=f"Теорія P(A) = {p_theory}")
    plt.xscale('log')
    plt.xlabel("Кількість випробувань N (log scale)")
    plt.ylabel("Відносна частота W(A)")
    plt.title("Блок 1: Демонстрація Закону великих чисел")
    plt.grid(True, which="both", ls="--")
    plt.legend()
    os.makedirs("graphics", exist_ok=True)
    plt.savefig("graphics/block1_lln.png", dpi=300)
    plt.close()
    print("-> Графік збережено в graphics/block1_lln.png\n")

if __name__ == "__main__":
    run_block_1()