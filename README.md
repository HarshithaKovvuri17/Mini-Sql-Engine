# Mini In-Memory SQL Engine (Python)

## Overview
This project implements a simplified in-memory SQL query engine using Python.
It loads CSV files into memory and executes basic SQL queries to demonstrate
how databases internally process SELECT, WHERE, and COUNT operations.

The engine runs as an interactive command-line application (REPL).

---

## Features
- Load CSV files into memory (list of dictionaries)
- SELECT * or specific columns
- WHERE clause with a single condition
- COUNT(*) and COUNT(column)
- Interactive CLI
- Clear error handling

---

## Setup and Run

### Prerequisites
- Python 3.8 or higher

### Run the Application
```bash
python cli.py
```

Type `exit` or `quit` to exit the CLI.

---

## Supported SQL Grammar

### SELECT
```sql
SELECT *
SELECT column1, column2
```

### WHERE (single condition only)
```sql
WHERE age > 25
WHERE country = 'USA'
WHERE salary <= 60000
```

### COUNT
```sql
SELECT COUNT(*)
SELECT COUNT(age)
```

---

## Example Queries
```sql
SELECT * FROM users;
SELECT name, age FROM users WHERE age > 25;
SELECT COUNT(*) FROM users;
SELECT COUNT(age) FROM users WHERE country = 'USA';
```

---

## Project Structure
```
mini-sql-engine/
├── cli.py        # Command-line interface (REPL)
├── parser.py     # SQL parsing logic
├── engine.py     # Query execution engine
├── README.md
└── data/
    ├── users.csv
    └── employees.csv
```

---

## Limitations
- Only SELECT queries are supported
- No JOIN, GROUP BY, or ORDER BY
- Only one WHERE condition is allowed

---

## Purpose
This project is intended for educational purposes to understand the internal
working of SQL query parsing and execution.
