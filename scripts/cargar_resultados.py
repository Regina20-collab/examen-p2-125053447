import sys, subprocess
rows = [l.strip().split("\t") for l in open(sys.argv[1]) if l.strip()]
sql = "INSERT INTO resultados VALUES " + ",".join(f"('{p}',{v})" for p, v in rows) + " ON CONFLICT (producto) DO UPDATE SET ingreso_total=EXCLUDED.ingreso_total;"
subprocess.run(["docker","compose","exec","-T","db","sh","-c",
  'psql -U "$POSTGRES_USER" -d "$POSTGRES_DB"'], input=sql.encode(), check=True)
