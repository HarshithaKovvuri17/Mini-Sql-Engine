from parser import parse_sql
from engine import execute_query

def print_result(rows):
    if not rows:
        print("Empty result")
        return

    headers = rows[0].keys()
    print(" | ".join(headers))
    print("-" * 40)

    for row in rows:
        print(" | ".join(str(v) for v in row.values()))


def main():
    while True:
        query = input("sql> ")

        if query.lower() in ("exit", "quit"):
            break

        try:
            parsed = parse_sql(query)
            result = execute_query(parsed)
            print_result(result)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
