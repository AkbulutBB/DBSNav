import numpy as np
import matplotlib.pyplot as plt

# Define the start and end points of the vectors for STN, Gpi, and Vim separately
stn_vectors = [
    {"plan_end": np.array([135.56, 135.72, 145.93]), "plan_start": np.array([163.09, 104.53, 216.53]), "actual_end": np.array([135.37, 134.89, 143.31]), "actual_start": np.array([155.48, 114.11, 190.18]), "label": "STN L"},
    {"plan_end": np.array([111.56, 135.46, 145.93]), "plan_start": np.array([84.96, 104.15, 217.03]), "actual_end": np.array([113.48, 133.66, 142.72]), "actual_start": np.array([92.64, 107.81, 200.59]), "label": "STN R"}
]

gpi_vectors = [
    {"plan_end": np.array([146.38, 130.16, 148.81]), "plan_start": np.array([157.85, 80.26, 195.5]), "actual_end": np.array([140.93, 129.7, 152.69]), "actual_start": np.array([155, 93.66, 180.83]), "label": "Gpi L"},
    {"plan_end": np.array([100.86, 129.67, 148.82]), "plan_start": np.array([90.21, 78.16, 201.21]), "actual_end": np.array([100.89, 127.49, 148.09]), "actual_start": np.array([93.79, 87.45, 189.82]), "label": "Gpi R"}
]

vim_vectors = [
    {"plan_end": np.array([137.08, 138.39, 149.61]), "plan_start": np.array([186.95, 143.55, 210.96]), "actual_end": np.array([136.91, 139.07, 147.11]), "actual_start": np.array([173.57, 140.29, 191.14]), "label": "Vim L"},
    {"plan_end": np.array([109.98, 138.1, 149.61]), "plan_start": np.array([57.71, 142.65, 209.28]), "actual_end": np.array([111.69, 135.36, 145.21]), "actual_start": np.array([71.87, 138.86, 195.34]), "label": "Vim R"}
]

def plot_vectors_with_bigger_labels(vectors, title):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    for vec in vectors:
        # Calculate the plan vector
        plan_vector = vec["plan_end"] - vec["plan_start"]
        # Calculate the actual vector
        actual_vector = vec["actual_end"] - vec["actual_start"]
        
        # Plot the plan vector
        ax.quiver(vec["plan_start"][0], vec["plan_start"][1], vec["plan_start"][2],
                  plan_vector[0], plan_vector[1], plan_vector[2],
                  arrow_length_ratio=0.05, color='b', label=f'Plan {vec["label"]}')
        
        # Plot the actual vector
        ax.quiver(vec["actual_start"][0], vec["actual_start"][1], vec["actual_start"][2],
                  actual_vector[0], actual_vector[1], actual_vector[2],
                  arrow_length_ratio=0.05, color='r', label=f'Actual {vec["label"]}')
        
        # Add labels to the vectors with further adjustment and non-overlapping positioning
        ax.text(vec["plan_start"][0], vec["plan_start"][1], vec["plan_start"][2], f'Plan {vec["label"]}', color='blue', fontsize=12)
        ax.text(vec["actual_start"][0], vec["actual_start"][1], vec["actual_start"][2], f'Actual {vec["label"]}', color='red', fontsize=12)

    # Labels and title
    ax.set_title(f'3D Vector Field of Planned vs Actual Electrode Placement: {title}', fontsize=14)
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_zlabel('Z', fontsize=12)

    # Fit all vectors within the plot limits
    all_x = np.concatenate([[vec["plan_start"][0], vec["plan_end"][0], vec["actual_start"][0], vec["actual_end"][0]] for vec in vectors])
    all_y = np.concatenate([[vec["plan_start"][1], vec["plan_end"][1], vec["actual_start"][1], vec["actual_end"][1]] for vec in vectors])
    all_z = np.concatenate([[vec["plan_start"][2], vec["plan_end"][2], vec["actual_start"][2], vec["actual_end"][2]] for vec in vectors])

    ax.set_xlim([round(min(all_x) / 10) * 10 - 10, round(max(all_x) / 10) * 10 + 10])
    ax.set_ylim([round(min(all_y) / 10) * 10 - 10, round(max(all_y) / 10) * 10 + 10])
    ax.set_zlim([round(min(all_z) / 10) * 10 - 10, round(max(all_z) / 10) * 10 + 10])

    # Set the intervals for all axes
    ax.set_xticks(np.arange(round(min(all_x) / 10) * 10 - 10, round(max(all_x) / 10) * 10 + 10, 10))
    ax.set_yticks(np.arange(round(min(all_y) / 10) * 10 - 10, round(max(all_y) / 10) * 10 + 10, 10))
    ax.set_zticks(np.arange(round(min(all_z) / 10) * 10 - 10, round(max(all_z) / 10) * 10 + 10, 10))

    # Change the azimuth angle to view from the side
    ax.view_init(elev=20., azim=90)

    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.show()

# Plot STN vectors with 10 mm intervals, larger plots, and bigger labels
plot_vectors_with_bigger_labels(stn_vectors, "STN")

# Plot Gpi vectors with 10 mm intervals, larger plots, and bigger labels
plot_vectors_with_bigger_labels(gpi_vectors, "Gpi")

# Plot Vim vectors with 10 mm intervals, larger plots, and bigger labels
plot_vectors_with_bigger_labels(vim_vectors, "Vim")
