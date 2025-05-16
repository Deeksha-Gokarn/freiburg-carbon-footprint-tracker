import duckdb

# Connect to DuckDB
con = duckdb.connect('python/carbon_footprint.db')

# Correct query with matching columns
result = con.execute("""
    SELECT
        a.activity,
        a.unit,
        a.amount,
        e.co2_per_unit,
        ROUND(a.amount * e.co2_per_unit, 2) AS total_co2e_kg
    FROM activities a
    JOIN emissions e
      ON a.activity = e.activity
""").fetchdf()

# Show the result
print(result)
