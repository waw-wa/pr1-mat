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
    # Створення папки для збередення графіків, якщо її не існує
    os.makedirs("graphics", exist_ok=True)
    plt.savefig("graphics/block1_lln.png", dpi=300)
    plt.close()
    print("-> Графік збережено в graphics/block1_lln.png\n")

# -------------------------------------------------------------
# БЛОК 3: Метод Монте-Карло (Оцінка числа pi)
# -------------------------------------------------------------
def run_block_3():
    print("=== БЛОК 3: Оцінка числа Pi методом Монте-Карло ===")
    sample_sizes = [10, 100, 1000, 10000, 100000, 1000000]
    pi_estimates = []
    
    for N in sample_sizes:
        inside_circle = 0
        for _ in range(N):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            if x*x + y*y <= 1.0:
                inside_circle += 1
        pi_est = 4.0 * inside_circle / N
        err = abs(pi_est - math.pi)
        pi_estimates.append(pi_est)
        print(f"N = {N:>7} | Pi_оцінка = {pi_est:.6f} | Math.pi = {math.pi:.6f} | Похибка = {err:.6f}")
        
    # Побудова графіка для Блоку 3
    plt.figure(figsize=(9, 5))
    plt.plot(sample_sizes, pi_estimates, marker='s', color='darkgreen', label="Оцінка Pi")
    plt.axhline(y=math.pi, color='crimson', linestyle='--', label=f"Константа math.pi ({math.pi:.4f})")
    plt.xscale('log')
    plt.xlabel("Кількість точок N (log scale)")
    plt.ylabel("Значення Pi")
    plt.title("Блок 3: Збіжність методу Монте-Карло до числа Pi")
    plt.grid(True, which="both", ls="--")
    plt.legend()
    plt.savefig("graphics/block3_pi_convergence.png", dpi=300)
    plt.close()
    print("-> Графік збережено в graphics/block3_pi_convergence.png\n")

# -------------------------------------------------------------
# БЛОК 4: Професійні комплексні задачі (Класифікатор )
# -------------------------------------------------------------

def run_block_4():
    print("=== БЛОК 4: Професійна задача (Варіант 4 - Класифікатор) ===")
    total = 5000
    correct = 4600
    error = 400
    
    p_correct = correct / total
    p_error = error / total
    
    print(f"Всього об'єктів: {total}")
    print(f"P(Correct) = {correct}/{total} = {p_correct:.4f} ({p_correct*100:.1f}%)")
    print(f"P(Error)   = {error}/{total} = {p_error:.4f} ({p_error*100:.1f}%)")
    print(f"Перевірка повної групи: P(Correct) + P(Error) = {p_correct + p_error:.1f}\n")

if __name__ == "__main__":
    run_block_1()    run_block_1()    # Фіксуємо seed для відтворюваності, або можна прибрати для випадковості
    random.seed(42)
    run_block_1()
    run_block_3()
    run_block_4()