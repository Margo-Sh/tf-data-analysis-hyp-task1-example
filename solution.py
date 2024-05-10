import pandas as pd
import numpy as np
import scipy.stats as sps


chat_id = 334982039 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.06

    x_mean = x_success / x_cnt
    y_mean = y_success / y_cnt
    x_var = x_mean * (1 - x_mean) / x_cnt
    y_var = y_mean * (1 - y_mean) / y_cnt

    std = np.sqrt(x_var + y_var)
    z_stat = sps.norm.ppf(1-alpha)
    # Ваш ответ, True или False
    return y_mean - x_mean > std * z_stat
