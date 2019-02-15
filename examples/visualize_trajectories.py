# This is not needed if the trackintel library is installed. ==================
import sys
sys.path.append("..")
sys.path.append("../trackintel")
# =============================================================================

import logging

import matplotlib.pyplot as plt
import trackintel as ti


logging.basicConfig(filename='log/visualize_trajectories.log', level=logging.INFO, filemode='w')

# GPSies trajectory.
positionfixes = ti.read_positionfixes_csv('data/gpsies_trajectory.csv', sep=';')
ti.plot_positionfixes(positionfixes, out_filename='out/gpsies_trajectory_positionfixes.png', plot_osm=True)

# Geolife trajectory.
positionfixes = ti.read_positionfixes_csv('data/geolife_trajectory.csv', sep=';')
ti.plot_positionfixes(positionfixes, out_filename='out/geolife_trajectory_positionfixes.png', plot_osm=False)