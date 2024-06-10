import numpy as np
import pandas as pd

def calculate_distance_point_to_line(point, line_start, line_end):
    line_vec = line_end - line_start
    point_vec = point - line_start
    cross_prod = np.cross(line_vec, point_vec)
    distance = np.linalg.norm(cross_prod) / np.linalg.norm(line_vec)
    return distance

# Define the vectors for STN, Gpi, and Vim
vectors = {
    "STN": [
        {"plan_end": np.array([135.56, 135.72, 145.93]), "plan_start": np.array([163.09, 104.53, 216.53]), "actual_end": np.array([135.37, 134.89, 143.31]), "actual_start": np.array([155.48, 114.11, 190.18]), "label": "STN L"},
        {"plan_end": np.array([111.56, 135.46, 145.93]), "plan_start": np.array([84.96, 104.15, 217.03]), "actual_end": np.array([113.48, 133.66, 142.72]), "actual_start": np.array([92.64, 107.81, 200.59]), "label": "STN R"}
    ],
    "Gpi": [
        {"plan_end": np.array([146.38, 130.16, 148.81]), "plan_start": np.array([157.85, 80.26, 195.5]), "actual_end": np.array([140.93, 129.7, 152.69]), "actual_start": np.array([155, 93.66, 180.83]), "label": "Gpi L"},
        {"plan_end": np.array([100.86, 129.67, 148.82]), "plan_start": np.array([90.21, 78.16, 201.21]), "actual_end": np.array([100.89, 127.49, 148.09]), "actual_start": np.array([93.79, 87.45, 189.82]), "label": "Gpi R"}
    ],
    "Vim": [
        {"plan_end": np.array([137.08, 138.39, 149.61]), "plan_start": np.array([186.95, 143.55, 210.96]), "actual_end": np.array([136.91, 139.07, 147.11]), "actual_start": np.array([173.57, 140.29, 191.14]), "label": "Vim L"},
        {"plan_end": np.array([109.98, 138.1, 149.61]), "plan_start": np.array([57.71, 142.65, 209.28]), "actual_end": np.array([111.69, 135.36, 145.21]), "actual_start": np.array([71.87, 138.86, 195.34]), "label": "Vim R"}
    ]
}

def calculate_trajectory_distances(vectors):
    distances = []
    for target, target_vectors in vectors.items():
        for vec in target_vectors:
            plan_start_distance = calculate_distance_point_to_line(vec["plan_start"], vec["actual_start"], vec["actual_end"])
            plan_end_distance = calculate_distance_point_to_line(vec["plan_end"], vec["actual_start"], vec["actual_end"])
            distances.append({"label": vec["label"], "target": target, "plan_start_distance": plan_start_distance, "plan_end_distance": plan_end_distance})
    return distances

trajectory_distances = calculate_trajectory_distances(vectors)
trajectory_distances_df = pd.DataFrame(trajectory_distances)

# Round the distances to 2 decimal places
trajectory_distances_df_rounded = trajectory_distances_df.round({'plan_start_distance': 2, 'plan_end_distance': 2})

import ace_tools as tools; tools.display_dataframe_to_user(name="Rounded Electrode Trajectory Distances", dataframe=trajectory_distances_df_rounded)
