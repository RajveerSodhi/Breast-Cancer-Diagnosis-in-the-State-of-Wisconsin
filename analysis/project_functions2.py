import pandas as pd

def load_and_process(filename):
    df = (
        pd.read_csv(filename)
        .drop(['id', 'Unnamed: 32'], axis = 1)
        .dropna()
        .sort_values(by = 'diagnosis', ascending = True)
        .reset_index(drop = True)
        .rename(columns = {'diagnosis': 'Diagnosis', 'radius_mean': 'Mean Radius', 'texture_mean': 'Mean Texture', 'perimeter_mean': 'Mean Perimeter', 'area_mean': 'Mean Area', 'smoothness_mean': 'Mean Smoothness', 'compactness_mean': 'Mean Compactness', 'concavity_mean': 'Mean Concavity', 'concave points_mean': 'Mean Concave Points', 'symmetry_mean': 'Mean Symmetry', 'fractal_dimension_mean': 'Mean Fractal Dimension', 'radius_se': 'Standard Error of Radius', 'texture_se': 'Standard Error of Texture', 'perimeter_se': 'Standard Error of Perimeter', 'area_se': 'Standard Error of Area', 'smoothness_se': 'Standard Error of Smoothness', 'compactness_se': 'Standard Error of Compactness', 'concavity_se': 'Standard Error of Concavity', 'concave points_se': 'Standard Error of Concave Points', 'symmetry_se': 'Standard Error of Symmetry', 'fractal_dimension_se': 'Standard Error of Fractal Dimension', 'radius_worst': 'Worst Radius', 'texture_worst': 'Worst Texture', 'perimeter_worst': 'Worst Perimeter', 'area_worst': 'Worst Area', 'smoothness_worst': 'Worst Smoothness', 'compactness_worst': 'Worst Compactness', 'concavity_worst': 'Worst Concavity', 'concave points_worst': 'Worst Concave Points', 'symmetry_worst': 'Worst Symmetry', 'fractal_dimension_worst': 'Worst Fractal Dimension'})
        .applymap(lambda x: "Malignant" if (x == "M") else ("Benign" if (x == "B") else x))
    )
        
    return df

def load_and_process_for_tableau_and_export(filename):
    df = (
        pd.read_csv(filename)
        .drop(['Unnamed: 32'], axis = 1)
        .dropna()
        .sort_values(by = 'diagnosis', ascending = True)
        .reset_index(drop = True)
        .rename(columns = {'diagnosis': 'Diagnosis', 'radius_mean': 'Mean Radius', 'texture_mean': 'Mean Texture', 'perimeter_mean': 'Mean Perimeter', 'area_mean': 'Mean Area', 'smoothness_mean': 'Mean Smoothness', 'compactness_mean': 'Mean Compactness', 'concavity_mean': 'Mean Concavity', 'concave points_mean': 'Mean Concave Points', 'symmetry_mean': 'Mean Symmetry', 'fractal_dimension_mean': 'Mean Fractal Dimension', 'radius_se': 'Standard Error of Radius', 'texture_se': 'Standard Error of Texture', 'perimeter_se': 'Standard Error of Perimeter', 'area_se': 'Standard Error of Area', 'smoothness_se': 'Standard Error of Smoothness', 'compactness_se': 'Standard Error of Compactness', 'concavity_se': 'Standard Error of Concavity', 'concave points_se': 'Standard Error of Concave Points', 'symmetry_se': 'Standard Error of Symmetry', 'fractal_dimension_se': 'Standard Error of Fractal Dimension', 'radius_worst': 'Worst Radius', 'texture_worst': 'Worst Texture', 'perimeter_worst': 'Worst Perimeter', 'area_worst': 'Worst Area', 'smoothness_worst': 'Worst Smoothness', 'compactness_worst': 'Worst Compactness', 'concavity_worst': 'Worst Concavity', 'concave points_worst': 'Worst Concave Points', 'symmetry_worst': 'Worst Symmetry', 'fractal_dimension_worst': 'Worst Fractal Dimension'})
        .applymap(lambda x: 1 if (x == "M") else (0 if (x == "B") else x))
    )
    
    df.melt(id_vars = ["id"]).to_csv("../data/processed/processed_data2_1.csv")