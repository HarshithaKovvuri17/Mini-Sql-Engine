def parse_sql(query):
    """
    Parses SQL with:
    SELECT
    FROM
    optional WHERE
    Supports COUNT(*), COUNT(column)
    """

    query = query.strip().rstrip(";")

    if not query.upper().startswith("SELECT"):
        raise ValueError("Only SELECT queries are supported")

    # Split SELECT and FROM
    try:
        select_part, rest = query.split("FROM")
    except ValueError:
        raise ValueError("Invalid SQL: missing FROM clause")

    # Parse SELECT
    select_part = select_part.replace("SELECT", "").strip()

    if select_part.upper().startswith("COUNT"):
        inside = select_part[6:-1].strip()
        select_cols = ["COUNT", inside]
    elif select_part == "*":
        select_cols = ["*"]
    else:
        select_cols = [c.strip() for c in select_part.split(",")]

    # Parse FROM and WHERE
    where_clause = None
    if "WHERE" in rest.upper():
        from_part, where_part = rest.split("WHERE")
        table_name = from_part.strip()

        where_part = where_part.strip()
        operators = ["<=", ">=", "!=", "=", "<", ">"]

        for op in operators:
            if op in where_part:
                col, val = where_part.split(op)
                where_clause = {
                    "column": col.strip(),
                    "operator": op,
                    "value": val.strip().strip("'")
                }
                break
        else:
            raise ValueError("Invalid WHERE condition")
    else:
        table_name = rest.strip()

    return {
        "select": select_cols,
        "table": table_name,
        "where": where_clause
    }
