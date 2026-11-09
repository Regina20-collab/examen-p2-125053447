import os, time
import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)

def conn():
    return psycopg2.connect(host="db", dbname=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"], password=os.environ["POSTGRES_PASSWORD"])

def init():
    for _ in range(30):
        try:
            c = conn(); cur = c.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS resultados (producto TEXT PRIMARY KEY, ingreso_total NUMERIC)")
            c.commit(); c.close(); return
        except Exception:
            time.sleep(2)

@app.get("/resultados")
def todos():
    c = conn(); cur = c.cursor()
    cur.execute("SELECT producto, ingreso_total FROM resultados ORDER BY ingreso_total DESC")
    r = [{"producto": a, "ingreso_total": float(b)} for a, b in cur.fetchall()]
    c.close(); return jsonify(r)

@app.get("/resultados/<producto>")
def uno(producto):
    c = conn(); cur = c.cursor()
    cur.execute("SELECT producto, ingreso_total FROM resultados WHERE producto=%s", (producto,))
    r = cur.fetchone(); c.close()
    if not r: return jsonify({"error": "no existe"}), 404
    return jsonify({"producto": r[0], "ingreso_total": float(r[1])})

@app.post("/resultados")
def crear():
    d = request.get_json()
    c = conn(); cur = c.cursor()
    cur.execute("INSERT INTO resultados VALUES (%s,%s)", (d["producto"], d["ingreso_total"]))
    c.commit(); c.close(); return jsonify(d), 201

@app.delete("/resultados/<producto>")
def borrar(producto):
    c = conn(); cur = c.cursor()
    cur.execute("DELETE FROM resultados WHERE producto=%s", (producto,))
    c.commit(); c.close(); return "", 204

if __name__ == "__main__":
    init()
    app.run(host="0.0.0.0", port=5000)
