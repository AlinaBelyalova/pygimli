import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
import numpy as np

def finalcycle():
    
    fig, ax = plt.subplots(figsize=(24, 10))  # Увеличиваем размер фигуры
    ax.set_xlim(-17, 30)  # Увеличиваем пределы по оси X
    ax.set_ylim(0, 15)  # Увеличиваем пределы по оси Y
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal', 'box')
    
    colors = {
        'Загрузка данных': '#A6CEE3',
        'Менеджер инверсии': '#1F78B4',
        'Установка параметров': '#B2DF8A',
        'Инверсия': '#33A02C',
        'Выгрузка данных': '#FB9A99',
        'Проверка и ошибки': '#E31A1C'
    }
    
    def add_gradient(ax, x, y, width, height, color1, color2):
        gradient = np.zeros((100, 1, 4))
        gradient[:, :, :3] = np.linspace(np.array(mcolors.to_rgba(color1)[:3]), np.array(mcolors.to_rgba(color2)[:3]), 100)[:, None, :]
        gradient[:, :, 3] = 1
        ax.imshow(gradient, aspect='auto', extent=(x, x + width, y, y + height), zorder=-1)
    
    def add_block(ax, x, y, width, height, color1, color2, title, details):
        add_gradient(ax, x, y, width, height, color1, color2)
        rect = mpatches.FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.3", linewidth=1.5, edgecolor='gray', facecolor='none')
        ax.add_patch(rect)
        ax.text(x + width / 2, y + height * 0.65, title, ha='center', va='center', fontsize=12, fontweight='bold', color='black', zorder=1)
        ax.text(x + width / 2, y + height * 0.35, details, ha='center', va='center', fontsize=10, color='black', zorder=1)
    
    def add_arrow(ax, start, end, color='gray', connectionstyle="arc3,rad=0.05"):
        arrow = mpatches.FancyArrowPatch(posA=start, posB=end, connectionstyle=connectionstyle, color=color, linewidth=2, arrowstyle='-|>', mutation_scale=10)
        ax.add_patch(arrow)
    
    block_width = 4.5  # Уменьшаем ширину блоков
    block_height = 2  # Уменьшаем высоту блоков
    y_start = 9
    spacing = 3  # Уменьшаем расстояние между блоками
    
    # Загрузка данных
    add_block(ax, -15, y_start, block_width, block_height, '#8EC6C5', '#E0F7FA', 
              'Загрузка данных', 'pg.load \nФайл: 38_p.sgt')
    add_block(ax, -15, y_start - spacing, block_width, block_height, '#F48FB1', '#FCE4EC', 
              'Проверка данных', 'Формат')
    
    add_arrow(ax, (-9.5, y_start + block_height / 2), (-7, y_start + block_height / 2))
    
    # Менеджер инверсии
    add_block(ax, -6, y_start, block_width, block_height, '#1E88E5', '#BBDEFB', 
              'Менеджер \nинверсии', '\nTravelTimeManager\nПодготовка данных')
    add_block(ax, -6, y_start - spacing, block_width, block_height, '#F06292', '#F8BBD0', 
              'Логи ошибок', 'Ограничения по ошибкам \nУдаление данных <0')
    
    add_arrow(ax, (-0.5, y_start + block_height / 2), (4, y_start + block_height / 2))
    
    # Установка параметров
    add_block(ax, 5, y_start, block_width, block_height, '#80CBC4', '#E0F2F1', 
              'Установка \nпараметров', 'lam, dPhi, vTop...')
    
    add_arrow(ax, (10, y_start + block_height / 2), (14.5, y_start + 1))
    
    # Инверсия
    add_block(ax, 15, y_start, block_width, block_height, '#388E3C', '#C8E6C9', 
              'Инверсия', 'mgr.invert')
    
    add_arrow(ax, (20, y_start + block_height / 2), (23.5, y_start + block_height / 2))
    
    # Выгрузка данных
    add_block(ax, 24, y_start, block_width, block_height, '#EF9A9A', '#FFEBEE', 
              'Визуализация', 'mgr.showData\nshowFit, showResult')
    
    # Обратная стрелка от визуализации к установке параметров
    # Стрелка огибает все блоки сверху
    add_arrow(ax, (21.7, y_start + block_height / 3), (1.7, y_start + block_height / 3), connectionstyle="arc3,rad=-1.0")
    
    plt.title('Блок-схема проекта', fontsize=18, pad=20)
    plt.show()
