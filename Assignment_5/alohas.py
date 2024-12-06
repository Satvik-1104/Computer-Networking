import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pure_aloha_data = pd.read_excel('pure_aloha_experiment.xlsx')
slotted_aloha_data = pd.read_excel('slotted_aloha_experiment.xlsx')
G_values_pure = pure_aloha_data['G'].values
S_experimental_pure = pure_aloha_data['S'].values
G_values_slotted = slotted_aloha_data['G'].values
S_experimental_slotted = slotted_aloha_data['S'].values

S_theoretical_pure_aloha = G_values_pure * np.exp(-2 * G_values_pure)
S_theoretical_slotted_aloha = G_values_slotted * np.exp(-G_values_slotted)

plt.figure(figsize=(10, 6))
plt.plot(G_values_pure, S_experimental_pure, 'o-', label='Experimental S (Pure Aloha)', color='blue')
plt.plot(G_values_pure, S_theoretical_pure_aloha, 's-', label='Theoretical S (Pure Aloha)', color='red')
plt.plot(G_values_slotted, S_experimental_slotted, 'o-', label='Experimental S (Slotted Aloha)', color='purple')
plt.plot(G_values_slotted, S_theoretical_slotted_aloha, 'd-', label='Theoretical S (Slotted Aloha)', color='green')
plt.title('G vs S (Experimental and Theoretical)')
plt.xlabel('Offered Load (G)')
plt.ylabel('Throughput (S)')
plt.legend()
plt.grid(True)
plt.show()