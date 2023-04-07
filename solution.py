import pandas as pd
import numpy as np

from scipy.stats import uniform


chat_id = 694905952 # Ваш chat ID, не меняйте название переменной

def exact_solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    # q = (X - 0.041) / (1 - t) + 0.041
    # q = (X - 0.041) / (1 - alpha / 2) + 0.041, q = (X - 0.041) / (alpha / 2) + 0.041
    
    alpha = 1 - p
    #loc = x.mean()
    n = len(x)
    return 2*x.mean() + 2 * (alpha / 2) * x.var() / n ** (1/2) - 0.041, 2*x.mean() + 2 * (1 - alpha / 2) * x.var() / n ** (1/2)  - 0.041
