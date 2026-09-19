import random

# -------------------------------------------------------------
# БЛОК 2: Варіант 4 (Задача про зустріч)
# -------------------------------------------------------------

def simulate_meeting_problem(N, T=60.0, tau=10.0):
    """
    Варіант 4: Геометрична ймовірність (Задача про зустріч).
    Час прибуття x, y розподілені рівномірно на [0, T], T = 60.
    Умова зустрічі: |x - y| <= tau, tau = 10.
    """
    meeting_count = 0
    
    for _ in range(N):
        x = random.uniform(0, T)
        y = random.uniform(0, T)
        if abs(x - y) <= tau:
            meeting_count += 1
            
    p_stat_meeting = meeting_count / N
    p_stat_no_meeting = 1.0 - p_stat_meeting
    
    # Теоретичні значення з методички
    p_theory_no_meeting = ((T - tau) / T) ** 2  # (50/60)^2 = 25/36 ≈ 0.6944
    p_theory_meeting = 1.0 - p_theory_no_meeting  # 11/36 ≈ 0.3056
    
    error_meeting = abs(p_stat_meeting - p_theory_meeting)
    error_no_meeting = abs(p_stat_no_meeting - p_theory_no_meeting)
    
    return {
        "N": N,
        "W_meeting": p_stat_meeting,
        "P_theory_meeting": p_theory_meeting,
        "error_meeting": error_meeting,
        "W_no_meeting": p_stat_no_meeting,
        "P_theory_no_meeting": p_theory_no_meeting,
        "error_no_meeting": error_no_meeting
    }

def run_block_2():
    print("=== БЛОК 2: Варіант 4 (Задача про зустріч) ===")
    sample_sizes = [100, 1000, 10000, 100000, 1000000]
    
    print(f"{'N':>8} | {'W(Зустріч)':>11} | {'P(Теорія)':>10} | {'Похибка':>10} | {'W(Немає)':>10} | {'Похибка':>10}")
    print("-" * 72)
    
    for N in sample_sizes:
        res = simulate_meeting_problem(N)
        print(f"{N:>8} | {res['W_meeting']:>11.5f} | {res['P_theory_meeting']:>10.5f} | {res['error_meeting']:>10.5f} | "
              f"{res['W_no_meeting']:>10.5f} | {res['error_no_meeting']:>10.5f}")

if __name__ == "__main__":
    run_block_2()