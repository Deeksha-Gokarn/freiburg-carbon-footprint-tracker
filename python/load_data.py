import duckdb
import pandas as pd

# Load CSVs
activities = pd.read_csv('data/your_activities.csv')
emissions = pd.read_csv('data/emission_factors.csv')

# Create DuckDB database
con = duckdb.connect('carbon_footprint.db')

# Register pandas DataFrames
con.register("activities_df", activities)
con.register("emissions_df", emissions)

# Create tables from the DataFrames
con.execute("CREATE OR REPLACE TABLE activities AS SELECT * FROM activities_df")
con.execute("CREATE OR REPLACE TABLE emissions AS SELECT * FROM emissions_df")

print("✅ Data loaded into DuckDB successfully.")
