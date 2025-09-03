import random
import time
import json
import redis

# Conexão com Redis
redis_client = redis.Redis(host="localhost", port=6379, db=0)

def gerar_dado():
    """Gera um dado fictício de telemetria de caminhão."""
    return {
        "truck_id": random.randint(1, 10),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "velocidade": round(random.uniform(40, 120), 2),
        "temperatura_motor": round(random.uniform(70, 120), 2),
        "combustivel": round(random.uniform(10, 100), 2),
        "localizacao": (
            round(random.uniform(-90, 90), 6),
            round(random.uniform(-180, 180), 6),
        ),
    }

def iniciar_producer():
    """Loop que gera dados e envia para as filas Redis."""
    while True:
        dado = gerar_dado()
        dado_json = json.dumps(dado)

        # Envia para duas filas: banco de dados e alertas
        redis_client.lpush("fila_dados", dado_json)
        redis_client.lpush("fila_alertas", dado_json)

        print(f"[PRODUCER] Novo dado enviado: {dado}")
        time.sleep(2)

if __name__ == "__main__":
    iniciar_producer()
