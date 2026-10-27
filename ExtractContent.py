import pandas as pd
from pathlib import Path

# FIND PATH TO CSV FILE
folder = Path(__file__).parent
csv_path = folder / "cuisinesAllData.csv"
cuisinesDf = pd.read_csv(csv_path, encoding="utf-8-sig")

columns = ["name", "url", "ingredients", "calories", "fat", "carbs", "protein", "prep_time", "cook_time", "total_time", "servings"]

cuisinesDf = cuisinesDf[columns]
output_path = folder / "cuisines.csv"
cuisinesDf.to_csv(output_path, index=False)

print(cuisinesDf.head())
print(f"Saved to: {output_path}")
