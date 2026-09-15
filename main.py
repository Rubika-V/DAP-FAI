import pandas as pd
import json

print("Starting Data Acquisition Pipeline...\n")

# 1. Read Sales CSV
sales = pd.read_csv("data/sample_sales.csv")
print("✅ Sales CSV loaded")

# 2. Read Employee Excel
employees = pd.read_excel("data/employee_corrections.xlsx")
print("✅ Employee Excel loaded")

# 3. Read Website JSON
with open("data/website_logs.json", "r") as file:
    website_data = json.load(file)

website = pd.DataFrame(website_data)

# Convert timestamp into date
website["date"] = pd.to_datetime(
    website["timestamp"]
).dt.strftime("%Y-%m-%d")

# Match website user ID with employee ID
website = website.rename(
    columns={"user_id": "employee_id"}
)

print("✅ Website JSON loaded")

# 4. Read Weather JSON
# 4. Read Weather JSON
with open("data/weather_changed.json", "r") as file:
    weather_data = json.load(file)

weather = pd.DataFrame(weather_data)

# Expected weather API columns
expected_columns = {
    "date",
    "location",
    "temperature",
    "rainfall"
}
# Known API field changes
field_aliases = {
    "temp": "temperature",
    "rain": "rainfall"
}

# Detect and report known schema changes before renaming
detected_changes = []

for old_field, standard_field in field_aliases.items():
    if old_field in weather.columns:
        detected_changes.append(
            f"{old_field} -> {standard_field}"
        )

if detected_changes:
    print("\n⚠️ Known API schema change detected:")
    for change in detected_changes:
        print("   ", change)

# Rename changed fields to the standard names
weather = weather.rename(columns=field_aliases)

actual_columns = set(weather.columns)

missing_columns = expected_columns - actual_columns
extra_columns = actual_columns - expected_columns

# Detect schema changes
if missing_columns or extra_columns:
    print("\n⚠️ SCHEMA CHANGE DETECTED!")

    if missing_columns:
        print("Missing columns:", missing_columns)

    if extra_columns:
        print("New/Unexpected columns:", extra_columns)

else:
    print("✅ Weather API schema validated")

print("✅ Weather data loaded")

# 5. Combine Sales + Employee
unified = sales.merge(
    employees,
    on="employee_id",
    how="left"
)

# 6. Combine Website Data
website_summary = (
    website.groupby(["employee_id", "date"])
    .agg(
        web_visits=("action", "count"),
        purchases=("action", lambda x: (x == "purchase").sum())
    )
    .reset_index()
)

unified = unified.merge(
    website_summary,
    on=["employee_id", "date"],
    how="left"
)

# 7. Combine Weather Data
unified = unified.merge(
    weather,
    on=["date", "location"],
    how="left"
)

# Fill missing website values
unified["web_visits"] = unified["web_visits"].fillna(0)
unified["purchases"] = unified["purchases"].fillna(0)

# 8. Save unified dataset
unified.to_csv(
    "unified_dataset.csv",
    index=False
)

print("\n🎉 PIPELINE COMPLETED!")
print("Final dataset:")
print(unified)

print("\n📊 Number of records:", len(unified))
print("📊 Number of columns:", len(unified.columns))
print("\n📁 Saved as: unified_dataset.csv")
