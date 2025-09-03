import sqlite3
import json
import redis
import os

# Caminho do banco dentro de src/database
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "database", "fleet_data.db")

# Conexão com Redis
redis_client = redis.Redis(host="localhost", port=6379, db=0)

def criar_tabela():
    """Cria a tabela de dados de frota, caso não exista."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dados_frota (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            truck_id INTEGER,
            timestamp TEXT,
            velocidade REAL,
            temperatura_motor REAL,
            combustivel REAL,
            latitude REAL,
            longitude REAL
        )
    """)
    conn.commit()
    conn.close()

def salvar_dado(dado):
    """Salva um registro no banco SQLite."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO dados_frota (truck_id, timestamp, velocidade, temperatura_motor, combustivel, latitude, longitude)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        dado["truck_id"],
        dado["timestamp"],
        dado["velocidade"],
        dado["temperatura_motor"],
        dado["combustivel"],
        dado["localizacao"][0],
        dado["localizacao"][1],
    ))
    conn.commit()
    conn.close()

def iniciar_consumer():
    """Consome dados do Redis e salva no banco."""
    criar_tabela()
    print("[CONSUMER] Aguardando dados...")

    while True:
        dado_serializado = redis_client.rpop("fila_dados")
        if dado_serializado:
            dado = json.loads(dado_serializado)
            salvar_dado(dado)
            print(f"[CONSUMER] Dado salvo no banco: {dado}")

if __name__ == "__main__":
    iniciar_consumer()
