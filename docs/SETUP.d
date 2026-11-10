
## 5. Database connection from Pyhton

uv add "psycopg[binary]" python-dotenv

Connection settings are reas from `.env` by `src/sports_data_pipeline/db.py`. Quick check:

      uv run python -c "from sports_data_pipeline.db import get_connection; c = get_connection(); print(c.execute('select current_database(), current_user').fetchone()); c.close()"

Expected output: `('sports_dw', 'sports')`.
