import random
import csv
import json
import os
from weld_primitives import ButtWeld, FilletWeld, EdgeWeld
from assembly import Assembly

def generate_primitives(n=100):
    primitives = []
    types = [ButtWeld, FilletWeld, EdgeWeld]
    for _ in range(n):
        cls = random.choice(types)
        length = random.uniform(50, 500)
        density = random.uniform(7.8, 8.5)
        strength = random.uniform(0.6, 1.0)
        if cls == ButtWeld:
            obj = cls(length, density, strength, thickness=random.uniform(3, 12))
        elif cls == FilletWeld:
            obj = cls(length, density, strength, leg=random.uniform(3, 10))
        else:
            obj = cls(length, density, strength, flange_width=random.uniform(5, 15))
        primitives.append(obj)
    return primitives

def generate_assemblies(num_assemblies=10, prims_per_assembly=10):
    all_prims = generate_primitives(num_assemblies * prims_per_assembly)
    assemblies = []
    for i in range(num_assemblies):
        asm = Assembly(f"Assembly_{i+1}")
        for _ in range(prims_per_assembly):
            asm.add_primitive(all_prims.pop())
        assemblies.append(asm)
    return assemblies

def save_to_csv(assemblies, filename="assemblies.csv"):
    os.makedirs("project9", exist_ok=True)
    filepath = os.path.join("project9", filename)
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["name", "num_primitives", "total_mass_g", "total_volume_mm3"])
        for asm in assemblies:
            writer.writerow([asm.name, len(asm.primitives), 
                             round(asm.calculate_total_mass(), 2),
                             round(asm.calculate_total_volume(), 2)])
    print(f"CSV сохранён: {filepath}")

def save_to_json(assemblies, filename="assemblies.json"):
    os.makedirs("project9", exist_ok=True)
    filepath = os.path.join("project9", filename)
    data = []
    for asm in assemblies:
        data.append({
            "name": asm.name,
            "num_primitives": len(asm.primitives),
            "total_mass_g": asm.calculate_total_mass(),
            "total_volume_mm3": asm.calculate_total_volume(),
            "primitives": [str(p) for p in asm.primitives]
        })
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"JSON сохранён: {filepath}")