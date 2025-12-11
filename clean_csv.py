import pandas as pd

file_path = 'Student_Grades.csv'
df = pd.read_csv(file_path)

def clean_data(df):
    df_clean = df.dropna()
    for col in df_clean.columns:
        df_clean = df_clean[pd.to_numeric(df_clean[col], errors='coerce').notnull()]
    return df_clean

df_clean = clean_data(df)

cleaned_path = 'Student_Grades_clean.csv'
df_clean.to_csv(cleaned_path, index=False)
print(f"Cleaned data saved to {cleaned_path}")
