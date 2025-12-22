import json
import pandas as pd
from tabulate import tabulate

# Load JSON data
with open("module3_processed_ehr.json", "r") as f:
    data = json.load(f)

# Optional: Add ICD-10 code if not already present
icd_map = {
    "Pneumonia": "J18.9",
    "Diabetes": "E11.9",
    "Hypertension": "I10",
    "Asthma": "J45.909",
    "COVID-19": "U07.1"
}

for patient in data:
    diagnosis = patient.get("diagnosis", "").strip()
    patient["icd10_code"] = icd_map.get(diagnosis, "Not Available")

# Convert JSON to DataFrame
df = pd.DataFrame(data)

# Optional: reorder columns
columns_order = ["patient_id", "age", "gender", "symptoms", "doctor_observations", "diagnosis", "icd10_code"]
df = df[columns_order]

# Display in table format in console
print(tabulate(df, headers='keys', tablefmt='grid'))

# Optional: save as CSV for presentation
df.to_csv("module3_output_table.csv", index=False)
