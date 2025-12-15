import csv
import os


def load_table(table_name):
    file_path = f"data/{table_name}.csv"

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Table '{table_name}' does not exist")

    with open(file_path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def apply_where(rows, where):
    if not where:
        return rows

    filtered = []

    col = where["column"]
    op = where["operator"]
    val = where["value"]

    for row in rows:
        if col not in row:
            raise ValueError(f"Column '{col}' does not exist")

        cell = row[col]
        if cell == "":
            continue

        try:
            cell_val = float(cell)
            compare_val = float(val)
        except ValueError:
            cell_val = cell
            compare_val = val

        condition = {
            "=": cell_val == compare_val,
            "!=": cell_val != compare_val,
            ">": cell_val > compare_val,
            "<": cell_val < compare_val,
            ">=": cell_val >= compare_val,
            "<=": cell_val <= compare_val,
        }

        if condition[op]:
            filtered.append(row)

    return filtered


def execute_query(parsed_query):
    rows = load_table(parsed_query["table"])
    rows = apply_where(rows, parsed_query["where"])

    select = parsed_query["select"]

    # COUNT aggregation
    if select[0] == "COUNT":
        if select[1] == "*":
            return [{"COUNT": len(rows)}]
        else:
            col = select[1]
            count = sum(1 for r in rows if r.get(col))
            return [{"COUNT": count}]

    # SELECT *
    if select == ["*"]:
        return rows

    # SELECT specific columns
    result = []
    for row in rows:
        projected = {}
        for col in select:
            if col not in row:
                raise ValueError(f"Column '{col}' does not exist")
            projected[col] = row[col]
        result.append(projected)

    return result
