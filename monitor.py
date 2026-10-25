import time


def uso_cpu():
    with open("/proc/stat") as arquivo:
        linha = arquivo.readline()

    valores = linha.split()[1:]

    usuario = int(valores[0])
    sistema = int(valores[2])
    idle = int(valores[3])

    total = sum(int(v) for v in valores)

    uso = ((total - idle) / total) * 100

    return uso


def temperatura_cpu():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp") as arquivo:
            temperatura = int(arquivo.read()) / 1000

        return temperatura

    except:
        return None


def carga_sistema():
    try:
        with open("/proc/loadavg") as arquivo:
            carga = arquivo.read().split()[0]

        return carga

    except:
        return "indisponível"


def processos():
    try:
        with open("/proc/loadavg") as arquivo:
            dados = arquivo.read().split()

        ativos, total = dados[3].split("/")

        return int(total)

    except:
        return 0


def resumo_monitor():
    cpu = uso_cpu()
    temperatura = temperatura_cpu()
    carga = carga_sistema()
    quantidade = processos()

    texto = f"""
📊 MONITOR DO PC

🧠 Uso da CPU: {cpu:.1f}%
⚙️ Carga do sistema: {carga}
📋 Processos: {quantidade}
"""

    if temperatura is not None:
        texto += f"🌡️ Temperatura: {temperatura:.1f}°C"
    else:
        texto += "🌡️ Temperatura: indisponível"

    return texto

