import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import generate_data
from sklearn.preprocessing import StandardScaler

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "sensor_data_cleaned.csv")
    
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        df = generate_data.generate_sensor_csv("sensor_data_cleaned.csv")
    
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df.set_index("timestamp", inplace=True)
    
    numeric_cols = ["temperature_c", "pressure_bar", "vibration_mm_s"]
    russian_names = ["Температура, °C", "Давление, бар", "Вибрация, мм/с"]
    
    # Вычисление статистик
    def compute_stats(series):
        return pd.Series({
            "среднее": series.mean(),
            "медиана": series.median(),
            "мода": series.mode().iloc[0] if not series.mode().empty else np.nan,
            "стандартное_отклонение": series.std(),
            "дисперсия": series.var(),
            "минимум": series.min(),
            "максимум": series.max(),
            "размах": series.max() - series.min(),
            "квартиль_1": series.quantile(0.25),
            "квартиль_3": series.quantile(0.75),
            "межквартильный_размах": series.quantile(0.75) - series.quantile(0.25)
        })
    
    stats_df = pd.DataFrame({col: compute_stats(df[col]) for col in numeric_cols})
    stats_path = os.path.join(script_dir, "statistics_summary.csv")
    stats_df.to_csv(stats_path)
    print("Статистика сохранена")
    
    # Гистограммы
    for col, name in zip(numeric_cols, russian_names):
        plt.figure(figsize=(10, 6))
        sns.histplot(df[col], bins=30, kde=True, color='steelblue', edgecolor='black', alpha=0.7)
        mean_val = df[col].mean()
        median_val = df[col].median()
        plt.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Среднее = {mean_val:.3f}')
        plt.axvline(median_val, color='green', linestyle='-', linewidth=2, label=f'Медиана = {median_val:.3f}')
        plt.xlabel(name)
        plt.ylabel('Частота')
        plt.title(f'Распределение параметра: {name}')
        plt.legend()
        hist_path = os.path.join(script_dir, f"hist_{col}.png")
        plt.tight_layout()
        plt.savefig(hist_path, dpi=150)
        plt.close()
    
    # Boxplot без отображения выбросов (кружочков)
    fig, axes = plt.subplots(1, 3, figsize=(15, 6))
    
    for i, (col, name) in enumerate(zip(numeric_cols, russian_names)):
        box_data = df[col].dropna()
        bp = axes[i].boxplot(box_data, vert=True, patch_artist=True, showmeans=True, meanline=True,
                            showfliers=False)
        axes[i].set_title(name)
        axes[i].set_ylabel('Значение')
        axes[i].grid(axis='y', linestyle='--', alpha=0.7)
        for patch in bp['boxes']:
            patch.set_facecolor('lightblue')
            patch.set_alpha(0.7)
    
    plt.suptitle('Ящики с усами для параметров датчиков', fontsize=14)
    boxplot_path = os.path.join(script_dir, "boxplot_all.png")
    plt.tight_layout()
    plt.savefig(boxplot_path, dpi=150)
    plt.close()
    
    # Boxplot с нормализацией
    fig, ax = plt.subplots(figsize=(10, 6))
    scaler = StandardScaler()
    df_normalized = pd.DataFrame(scaler.fit_transform(df[numeric_cols]), columns=numeric_cols)
    
    data_for_box = [df_normalized[col].dropna() for col in numeric_cols]
    bp = ax.boxplot(data_for_box, labels=russian_names, patch_artist=True, showmeans=True, meanline=True,
                   showfliers=False)
    
    for patch in bp['boxes']:
        patch.set_facecolor('lightblue')
        patch.set_alpha(0.7)
    
    ax.set_ylabel('Z-оценка')
    ax.set_title('Boxplot стандартизованных параметров')
    ax.axhline(y=0, color='gray', linestyle='-', alpha=0.5)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    boxplot_norm_path = os.path.join(script_dir, "boxplot_normalized.png")
    plt.tight_layout()
    plt.savefig(boxplot_norm_path, dpi=150)
    plt.close()
    
    # Диаграмма рассеяния
    x_col, y_col = "pressure_bar", "vibration_mm_s"
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    axes[0].scatter(df[x_col], df[y_col], alpha=0.3, s=10, c='steelblue')
    axes[0].set_xlabel("Давление (бар)")
    axes[0].set_ylabel("Вибрация (мм/с)")
    axes[0].set_title("Диаграмма рассеяния")
    axes[0].grid(True, alpha=0.3)
    
    z = np.polyfit(df[x_col], df[y_col], 1)
    p = np.poly1d(z)
    axes[0].plot(sorted(df[x_col]), p(sorted(df[x_col])), "r-", linewidth=2, label=f'Регрессия: y={z[0]:.3f}x+{z[1]:.3f}')
    axes[0].legend()
    
    hexbin = axes[1].hexbin(df[x_col], df[y_col], gridsize=30, cmap='YlOrRd', mincnt=1)
    axes[1].set_xlabel("Давление (бар)")
    axes[1].set_ylabel("Вибрация (мм/с)")
    axes[1].set_title("Плотность точек")
    plt.colorbar(hexbin, ax=axes[1], label='Количество точек')
    
    corr_val = df[x_col].corr(df[y_col])
    fig.suptitle(f'Зависимость вибрации от давления | Корреляция: {corr_val:.3f}', fontsize=12)
    
    scatter_path = os.path.join(script_dir, "scatter_pressure_vibration.png")
    plt.tight_layout()
    plt.savefig(scatter_path, dpi=150)
    plt.close()
    
    print(f"Готово. Коэффициент корреляции: {corr_val:.3f}")

if __name__ == "__main__":
    main()