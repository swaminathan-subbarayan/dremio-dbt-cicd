# file: flight_test.py
import sys
from pyarrow import flightsql

HOST = "localhost"
PORT = 32010            # <-- Flight SQL default
USER = "admin"
PASSWORD = "Madhan@C8d1647a@2013"
USE_SSL = False         # local CE typically doesn't use SSL

endpoint = f"{'grpc+tls' if USE_SSL else 'grpc'}://{HOST}:{PORT}"

try:
    client = flightsql.FlightSqlClient(endpoint)
    # Basic username/password authentication
    client.authenticate_basic(USER, PASSWORD)

    # Run a trivial query to confirm end-to-end
    stmt = client.execute("SELECT 1 AS ok")
    reader = client.fetch_all(stmt)
    table = reader.read_all()
    print(table.to_pandas())

    # Optional: list catalogs/spaces to prove metadata access
    stmt2 = client.execute("SELECT * FROM INFORMATION_SCHEMA.CATALOGS")
    reader2 = client.fetch_all(stmt2)
    t2 = reader2.read_all()
    print("Catalogs rows:", t2.num_rows)

    print("✅ Flight SQL connectivity succeeded.")
except Exception as e:
    print("❌ Flight SQL connectivity failed:", e)
    sys.exit(1)