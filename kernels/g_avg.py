GAMMA = (1.0, 2.176, 43.29, 589.4, 1936.6, 7.989e4)
N_DOM = 6
G_AVG_OVER_GN = sum(1.0 / g / g for g in GAMMA) / N_DOM

def g_avg_over_gn():
    return float(G_AVG_OVER_GN)
