

# Select all female bears and return their names and ages
select_all_female_bears_return_name_and_age = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    WHERE sex='F';
"""

# Select all bears with age greater than 3
select_bears_with_age_greater_than_3 = """
    SELECT *
    FROM bears
    WHERE age > 3;
"""

# Select the names of bears that are alive
select_names_of_alive_bears = """
    SELECT name
    FROM bears
    WHERE alive = true;
"""

# Select the count of bears for each color
select_count_of_bears_per_color = """
    SELECT color, COUNT(*) as count
    FROM bears
    GROUP BY color;
"""
