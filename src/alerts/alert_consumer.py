import json
import redis
import time

# Conexão com Redis
redis_client = redis.Redis(host="localhost", port=6379, db=0)

def verificar_alertas(dado):
    """Verifica condições críticas no dado recebido."""
    alertas = []

    if dado["velocidade"] > 100:
        alertas.append(f"🚨 Velocidade alta detectada: {dado['velocidade']} km/h")

    if dado["temperatura_motor"] > 110:
        alertas.append(f"🔥 Superaquecimento do motor: {dado['temperatura_motor']} °C")

    if dado["combustivel"] < 15:
        alertas.append(f"⛽ Nível de combustível baixo: {dado['combustivel']}%")

    return alertas

def iniciar_alert_consumer():
    """Consome dados do Redis e verifica alertas."""
    print("[ALERT CONSUMER] Monitorando dados em tempo real...")

    while True:
        dado_serializado = redis_client.rpop("fila_alertas")
        if dado_serializado:
            dado = json.loads(dado_serializado)
            alertas = verificar_alertas(dado)

            if alertas:
                print(f"[ALERT CONSUMER] ALERTAS para Truck {dado['truck_id']} ({dado['timestamp']}):")
                for alerta in alertas:
                    print("   " + alerta)
            else:
                print(f"[ALERT CONSUMER] Truck {dado['truck_id']} sem alertas.")

        time.sleep(1)

if __name__ == "__main__":
    iniciar_alert_consumer()
