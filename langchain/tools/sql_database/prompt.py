# flake8: noqa
QUERY_CHECKER = """
{query}
Double check the {dialect} query above for common mistakes, including:
- Using NOT IN with NULL values(Consider using IS NOT NULL instead)
- Using UNION when UNION ALL should have been used.
- Using BETWEEN for exclusive ranges.
- Data type mismatch in predicates.
- Properly quoting identifiers.
- Using the correct number of arguments for functions.
- Casting to the correct data type.
- Using the proper columns for joins.
- You cannot use specific date functions 'MONTH' and 'YEAR' in any clause in BigQuery. Instead, use the 'EXTRACT' function to extract the month and year.
- When using the 'BETWEEN' operator in BigQuery queries, ensure consistent data types for the start and end values to avoid errors. For example, you can use CAST(TIMESTAMP('YYYY-MM-DD') AS TIMESTAMP) to convert date strings to TIMESTAMP data type before using them in the BETWEEN clause.
- When casting values in BigQuery queries, ensure that the values being cast are compatible with the desired data type. For example, when working with 'TIMESTAMP' values, use the 'TIMESTAMP' function to explicitly convert date strings to 'TIMESTAMP' data type.
- When using the 'HAVING' clause in BigQuery queries, ensure that the expressions referenced in the HAVING clause are either grouped or aggregated.
- When using column aliases in BigQuery, you cannot reference them directly in the 'WHERE' or 'GROUP BY' clauses. Instead, use backticks "```" or leave the alias without any enclosing characters.
- When specifying data types in BigQuery, use 'STRING' instead of 'VARCHAR'.


If there are any of the above mistakes, rewrite the query. If there are no mistakes, just reproduce the original query."""
