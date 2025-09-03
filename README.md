# 🚛 IoT Fleet Monitoring System  

Este projeto simula um **sistema de monitoramento de frotas** utilizando conceitos de **IoT, mensageria e persistência de dados**.  
A aplicação gera dados fictícios de telemetria de caminhões (velocidade, combustível, localização, etc.), envia para uma fila no **Redis** e processa com consumidores que armazenam e analisam as informações.  

---

## ⚙️ Arquitetura  

- **Producer** → Gera dados de telemetria dos caminhões e envia para uma fila no Redis.  
- **Consumer** → Consome os dados da fila e salva no banco de dados **SQLite**.  
- **Alert Consumer** → Monitora os dados em tempo real e gera **alertas** em caso de condições críticas (ex: motor superaquecido, combustível baixo).  

Fluxo:  [Producer] -> Redis -> [Consumer] -> SQLite | -> [Alert Consumer]


---

## 📊 Funcionalidades  

- Geração de dados de telemetria (simulação IoT).  
- Processamento assíncrono com fila (**Redis**).  
- Persistência em banco de dados (**SQLite**).  
- Regras de alerta em tempo real:
  - Motor superaquecido  
  - Baixo combustível  
  - Velocidade excessiva  

---

## 🛠️ Tecnologias  

- **Python 3**  
- **Redis** (mensageria)  
- **SQLite** (banco de dados local)  

---

## 🚀 Como executar  

### 1. Clone o repositório  
```bash
git clone https://github.com/seu-usuario/iot-fleet-monitoring.git
cd iot-fleet-monitoring


