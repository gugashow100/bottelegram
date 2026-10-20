import requests
import random
import time

# DADOS DO BOT
TOKEN = "8844763739:AAFGhZTGCGKCBfdKM4lWXBxh1G_zQgxGy78"
CHAT_ID = "-1004367781281"

# Valores possíveis
valores = [
    "🔴 ROJO",
    "🔵 AZUL"
]

# Texto fixo
mensagem_fixa = """
🚨 ¡SEÑAL CONFIRMADA! OPORTUNIDAD DE ENTRADA 🚨

🎯 Acción: COMPRAR AHORA

🔗 Enlace del juego:
[Inserta el enlace aquí]

🔄 Estrategia de Recuperación (Gale):
Si esta entrada no se da a la primera, mantén la calma.
En la próxima señal, duplica el valor de tu apuesta para recuperar el monto anterior y asegurar la ganancia.

⚠️ Juega con Responsabilidad:
Las apuestas implican riesgos.
Haz una buena gestión de tu banca, respeta tus límites diarios y nunca uses dinero que sea esencial para tu presupuesto.

Prohibido para menores de 18 años.
"""

while True:
    valor_sorteado = random.choice(valores)

    mensagem = f"""
{valor_sorteado}

{mensagem_fixa}
"""

    try:
        resposta = requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            data={
                "chat_id": CHAT_ID,
                "text": mensagem
            }
        )

        print("Mensagem enviada!")
        print(resposta.text)

    except Exception as erro:
        print("Erro:", erro)

    # 240 segundos = 4 minutos
    time.sleep(240)
