# Helper Scripts

This directory contains utility scripts that assist with maintaining and processing the FOCUS specification documentation.

## Requirements

- Python 3.7+
- Dependencies listed in `requirements.txt`

### Installation

Before using any helper scripts, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Available Scripts

### sql_transpile.py

A Python script that finds SQL code blocks in Markdown files and transpiles them between different SQL dialects using SQLGlot.

#### Purpose

- Extract SQL code blocks from Markdown documentation
- Detect SQL dialects automatically or use provided hints
- Transpile SQL between different database dialects (BigQuery, Trino, T-SQL, etc.)
- Validate SQL syntax across different platforms

#### Usage

```bash
# Transpile all SQL blocks in markdown files to T-SQL
./sql_transpile.py ../*.md --to tsql

# List all SQL blocks without transpiling
./sql_transpile.py ../*.md --list

# Transpile with dialect preference for detection
./sql_transpile.py ../*.md --to bigquery --prefer trino

# Process specific files
./sql_transpile.py ../file1.md ../file2.md --to postgres
```

#### Options

- `files`: Markdown files or glob patterns to process
- `--to`: Target SQL dialect (default: ansi)
- `--prefer`: Preferred dialect for detection (can be used multiple times)
- `--list`: Only list SQL blocks found, don't transpile

#### Supported Dialects

BigQuery, Trino, Presto, DuckDB, MySQL, PostgreSQL, Snowflake, T-SQL, Spark, Hive, Redshift, SQLite, Oracle, and ANSI SQL.

#### Dialect Hints

You can specify a dialect hint in your SQL code blocks:

````markdown
```sql bigquery
SELECT * FROM dataset.table
```

```sql:trino
SELECT * FROM catalog.schema.table  
```
````
