import os
import platform
import shutil
import time


def cpu():
    try:
        with open("/proc/cpuinfo") as arquivo:
            for linha in arquivo:
                if linha.startswith("model name"):
                    return linha.split(":", 1)[1].strip()
    except:
        pass

    return platform.processor()


def nucleos():
    return os.cpu_count()


def ram():
    memoria = {}

    with open("/proc/meminfo") as arquivo:
        for linha in arquivo:
            partes = linha.split()

            if len(partes) >= 2:
                memoria[partes[0].rstrip(":")] = int(partes[1])

    total = memoria.get("MemTotal", 0)
    livre = memoria.get("MemAvailable", 0)

    usada = total - livre

    return total / 1024 / 1024, usada / 1024 / 1024


def armazenamento():
    total, usado, livre = shutil.disk_usage("/")

    return (
        total / 1024**3,
        usado / 1024**3,
        livre / 1024**3
    )


def sistema_operacional():
    return platform.system()


def kernel():
    return platform.release()


def arquitetura():
    return platform.machine()


def hostname():
    return platform.node()


def uptime():
    try:
        with open("/proc/uptime") as arquivo:
            segundos = float(arquivo.read().split()[0])

        horas = int(segundos // 3600)
        minutos = int((segundos % 3600) // 60)

        return horas, minutos

    except:
        return 0, 0


def resumo():
    memoria_total, memoria_usada = ram()
    disco_total, disco_usado, disco_livre = armazenamento()

    horas, minutos = uptime()

    return f"""
🖥️ INFORMAÇÕES DO COMPUTADOR

🧠 CPU: {cpu()}
🔢 Núcleos: {nucleos()}

🧮 RAM:
   Total: {memoria_total:.2f} GB
   Usada: {memoria_usada:.2f} GB

💾 Armazenamento:
   Total: {disco_total:.1f} GB
   Usado: {disco_usado:.1f} GB
   Livre: {disco_livre:.1f} GB

🐧 Sistema: {sistema_operacional()}
⚙️ Kernel: {kernel()}
📦 Arquitetura: {arquitetura()}
🖥️ Computador: {hostname()}

⏱️ Ligado há: {horas}h {minutos}min
"""

