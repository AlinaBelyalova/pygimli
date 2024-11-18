import numpy as np
import pygimli as pg

def export_mesh_data(mesh_filename, output_filename="mesh_data.txt"):
    """
    Экспортирует координаты X, Y центров ячеек и "Velocity" 
    из файла mesh PyGIMLI в текстовый файл.

    Args:
        mesh_filename: Путь к файлу mesh PyGIMLI
        output_filename: Имя выходного текстового файла.
    """

    mesh = pg.load(mesh_filename)
    export_data = []

    for i, cell in enumerate(mesh.cells()):
        center_x = cell.center().x()
        center_y = cell.center().y()
        velocity = mesh["Velocity"][i]
        export_data.append([center_x, center_y, velocity])

    export_data = np.array(export_data)
    np.savetxt(output_filename, export_data, fmt="%.6f", header="X Y Velocity")


