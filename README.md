# BMI585 – Kalman Filtering Project

This repository contains my BMI585 Kalman Filtering course project using HSP polysomnography (PSG) data to model heart rate (HR) dynamics with a 1D Kalman filter and an ARX extension with a respiration driver derived from PTAF.

## Contents
- **Kalman_Project.ipynb**  
  Main notebook with all code: data loading, preprocessing (HR + PTAF driver), model implementation (Model A / Model B), parameter tuning, and plots/results.

- **BMI585_Project_Report.pdf**   
  Written report with problem definition, model equations, experiment setup, results, and interpretation.

- **config.py**  
  Helper configuration (parameters) used by the notebook.

## Dataset location
The HSP dataset is stored on the cluster at:

`/opt/scratchspace/qli50/HSP`

> Note: The dataset files are not included in this GitHub repository.

## How to run
1. Make sure you have access to the HSP directory above (cluster access required).
2. Open `Kalman_Project.ipynb` and update any path variables (such as `ROOT`, `COHORT`, or file paths).
3. Run the notebook cells top to bottom.
