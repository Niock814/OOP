import matplotlib.pyplot as plt
import numpy as np
import os
from data_generator import generate_assemblies

def plot_mass_distribution(assemblies):
    os.makedirs("project9", exist_ok=True)
    
    masses = [asm.calculate_total_mass() for asm in assemblies]
    names = [asm.name for asm in assemblies]
    
    sort_idx = np.argsort(masses)
    masses_sorted = [masses[i] for i in sort_idx]
    names_sorted = [names[i] for i in sort_idx]
    
    plt.figure(figsize=(10, 6))
    bars = plt.barh(names_sorted, masses_sorted, color='steelblue', edgecolor='black', alpha=0.8)
    plt.title('Масса сборок', fontsize=14, fontweight='bold')
    plt.xlabel('Масса (г)', fontsize=12)
    plt.ylabel('Название сборки', fontsize=12)
    plt.grid(True, alpha=0.3, linestyle='--', axis='x')
    
    for bar, mass in zip(bars, masses_sorted):
        plt.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, 
                f'{mass:.1f} г', ha='left', va='center', fontsize=9)
    
    filepath = os.path.join("project9", 'mass_distribution.png')
    plt.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"График сохранён: {filepath}")

    
def plot_strength_vs_length(assemblies):
    os.makedirs("project9", exist_ok=True)
    lengths = []
    strengths = []
    for asm in assemblies:
        for p in asm.primitives:
            lengths.append(p.length)
            strengths.append(p.get_strength())
    
    plt.figure(figsize=(12, 6))
    plt.scatter(lengths, strengths, alpha=0.6, c='darkred', s=50)
    z = np.polyfit(lengths, strengths, 1)
    p = np.poly1d(z)
    plt.plot(sorted(lengths), p(sorted(lengths)), 'b--', alpha=0.8, label=f'Тренд: y={z[0]:.2f}x+{z[1]:.2f}')
    plt.title('Зависимость прочности от длины примитива', fontsize=14, fontweight='bold')
    plt.xlabel('Длина (мм)', fontsize=12)
    plt.ylabel('Прочность (усл. ед.)', fontsize=12)
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.legend()
    filepath = os.path.join("project9", 'strength_vs_length.png')
    plt.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"График сохранён: {filepath}")