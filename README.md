# FastAPI Shop Inventory

A modern inventory management API built with FastAPI, supporting both SQLite and MongoDB backends, Alembic migrations.

## Features
- Product and catalog management (CRUD)
- Repository pattern for easy backend switching (SQLite/MongoDB)
- Alembic migrations for database schema

## Requirements
- Python 3.11+
- [uv](https://github.com/astral-sh/uv) (for dependency management)
- Docker (optional, for containerized deployment)

## Local Development

1. **Install dependencies:**
   ```sh
   uv pip install --system
   ```

2. **Run Alembic migrations:**
   ```sh
   alembic upgrade head
   ```

3. **Start the FastAPI server:**
   ```sh
   uv run uvicorn app.main:app --reload
   ```

4. **API Docs:**
   Visit [http://localhost:8000/docs](http://localhost:8000/docs)

5. **to run tests with pytest:**
   ```
   uv run pytest -v
   ```

## Project Structure
- `app/` - Main application code (models, schemas, repositories, routers)
- `alembic/` - Alembic migration scripts
- `pyproject.toml` - Project dependencies
- `uv.lock` - uv dependency lock file

## Environment Variables
- Not required for SQLite. For MongoDB, see `app/repositories/mongo_repo.py` for connection details.

## License
MIT

