import sistema
import monitor


def responder(pergunta):
    pergunta = pergunta.lower().strip()

    # ==========================================================
    # 👤 IDENTIDADE
    # ==========================================================

    if "quem criou" in pergunta or "quem fez você" in pergunta:
        return "Eu fui criada pelo Pedro!. "

    if "quem é você" in pergunta or "o que é você" in pergunta:
        return "Eu sou a pAI, uma inteligência artificial local feita em Python. 🐧🤖"

    if "qual seu nome" in pergunta or "qual é seu nome" in pergunta:
        return "Meu nome é pAI. 🤖"

    if "o que você sabe fazer" in pergunta:
        return (
            "Eu consigo consultar informações do computador, "
            "responder perguntas simples e conversar com você. "
            "E ainda estou aprendendo! 🧠"
        )

    # ==========================================================
    # 👋 SAUDAÇÕES
    # ==========================================================

    if pergunta in [
        "oi",
        "olá",
        "ola",
        "bom dia",
        "boa tarde",
        "boa noite"
    ]:
        return "Olá! 😄 Como posso ajudar?"

    if "tudo bem" in pergunta or "como você está" in pergunta:
        return "Estou funcionando perfeitamente! 🐧🤖"

    # ==========================================================
    # 🙏 EDUCAÇÃO
    # ==========================================================

    if (
        "obrigado" in pergunta
        or "obrigada" in pergunta
        or "valeu" in pergunta
    ):
        return "De nada! 😄"

    if "por favor" in pergunta:
        return "Claro! 😄"

    # ==========================================================
    # 🖥️ RESUMO DO COMPUTADOR
    # ==========================================================

    if (
        "resumo do pc" in pergunta
        or "resumo do computador" in pergunta
        or "informações do pc" in pergunta
        or "informacoes do pc" in pergunta
        or "como está meu pc" in pergunta
        or "como esta meu pc" in pergunta
        or "status do pc" in pergunta
    ):
        return sistema.resumo() + "\n" + monitor.resumo_monitor()

    # ==========================================================
    # 🧠 CPU
    # ==========================================================

    if (
        "qual minha cpu" in pergunta
        or "qual é minha cpu" in pergunta
        or "qual minha processador" in pergunta
        or "qual é meu processador" in pergunta
        or "que processador eu tenho" in pergunta
        or "qual processador eu tenho" in pergunta
    ):
        return f"Seu processador é um {sistema.cpu()}. 🧠"

    if (
        "quantos núcleos" in pergunta
        or "quantos nucleos" in pergunta
        or "quantos cores" in pergunta
    ):
        return f"Seu processador tem {sistema.nucleos()} núcleos. 🔢"

    # ==========================================================
    # 📊 USO DA CPU
    # ==========================================================

    if "uso da cpu" in pergunta:
        uso = monitor.uso_cpu()
        return f"O uso atual da CPU é de {uso:.1f}%. 🧠"

    if "uso de cpu" in pergunta:
        uso = monitor.uso_cpu()
        return f"O uso atual da CPU é de {uso:.1f}%. 🧠"

    if "quanto da cpu" in pergunta:
        uso = monitor.uso_cpu()
        return f"O uso atual da CPU é de {uso:.1f}%. 🧠"

    if "quanto de cpu" in pergunta:
        uso = monitor.uso_cpu()
        return f"O uso atual da CPU é de {uso:.1f}%. 🧠"

    if "cpu estou usando" in pergunta:
        uso = monitor.uso_cpu()
        return f"O uso atual da CPU é de {uso:.1f}%. 🧠"

    if "cpu está usando" in pergunta:
        uso = monitor.uso_cpu()
        return f"O uso atual da CPU é de {uso:.1f}%. 🧠"

    if "cpu esta usando" in pergunta:
        uso = monitor.uso_cpu()
        return f"O uso atual da CPU é de {uso:.1f}%. 🧠"

    # ==========================================================
    # 🧮 RAM
    # ==========================================================

    if (
        "quanta ram" in pergunta
        or "quanto de ram" in pergunta
        or "memória ram" in pergunta
        or "memoria ram" in pergunta
    ):
        total, usada = sistema.ram()
        return f"Você tem {total:.2f} GB de RAM. 🧠"

    if (
        "ram estou usando" in pergunta
        or "ram usada" in pergunta
        or "uso da ram" in pergunta
        or "uso de ram" in pergunta
    ):
        total, usada = sistema.ram()
        return f"Você está usando aproximadamente {usada:.2f} GB de RAM. 📊"

    # ==========================================================
    # 💾 ARMAZENAMENTO
    # ==========================================================

    if (
        "quanto de hd" in pergunta
        or "tamanho do hd" in pergunta
        or "tamanho do disco" in pergunta
        or "quanto armazenamento" in pergunta
    ):
        total, usado, livre = sistema.armazenamento()
        return f"Seu armazenamento tem {total:.1f} GB no total. 💾"

    if (
        "espaço livre" in pergunta
        or "espaco livre" in pergunta
        or "hd livre" in pergunta
        or "disco livre" in pergunta
        or "quanto espaço tenho" in pergunta
        or "quanto espaco tenho" in pergunta
    ):
        total, usado, livre = sistema.armazenamento()
        return f"Você tem {livre:.1f} GB livres. 💾"

    if (
        "quanto estou usando do hd" in pergunta
        or "quanto estou usando do disco" in pergunta
        or "espaço usado" in pergunta
        or "espaco usado" in pergunta
    ):
        total, usado, livre = sistema.armazenamento()
        return f"Você está usando {usado:.1f} GB do armazenamento. 💾"

    # ==========================================================
    # 🌡️ TEMPERATURA
    # ==========================================================

    if (
        "temperatura" in pergunta
        or "temperatura da cpu" in pergunta
        or "temperatura do processador" in pergunta
    ):
        temperatura = monitor.temperatura_cpu()

        if temperatura is not None:
            return f"A temperatura da CPU está em {temperatura:.1f}°C. 🌡️"

        return (
            "Não consegui encontrar a temperatura da CPU "
            "através do monitor padrão. 🌡️"
        )

    # ==========================================================
    # 📋 PROCESSOS
    # ==========================================================

    if (
        "quantos processos" in pergunta
        or "quantidade de processos" in pergunta
        or "processos existem" in pergunta
    ):
        quantidade = monitor.processos()
        return f"Existem aproximadamente {quantidade} processos no sistema. 📋"

    # ==========================================================
    # 📈 CARGA DO SISTEMA
    # ==========================================================

    if (
        "carga do sistema" in pergunta
        or "load average" in pergunta
        or "carga do pc" in pergunta
    ):
        carga = monitor.carga_sistema()
        return f"A carga atual do sistema é {carga}. 📊"

    # ==========================================================
    # 🐧 SISTEMA OPERACIONAL
    # ==========================================================

    if (
        "qual sistema" in pergunta
        or "qual meu sistema" in pergunta
        or "qual sistema operacional" in pergunta
        or "qual linux" in pergunta
    ):
        return f"Você está usando {sistema.sistema_operacional()}. 🐧"

    # ==========================================================
    # ⚙️ KERNEL
    # ==========================================================

    if "qual kernel" in pergunta or "versão do kernel" in pergunta:
        return f"Seu kernel é {sistema.kernel()}. ⚙️"

    # ==========================================================
    # 📦 ARQUITETURA
    # ==========================================================

    if "arquitetura" in pergunta:
        return f"Seu sistema usa arquitetura {sistema.arquitetura()}. 📦"

    # ==========================================================
    # 🖥️ NOME DO COMPUTADOR
    # ==========================================================

    if (
        "nome do computador" in pergunta
        or "nome desse computador" in pergunta
        or "hostname" in pergunta
    ):
        return f"O nome do computador é {sistema.hostname()}. 🖥️"

    # ==========================================================
    # ⏱️ TEMPO LIGADO
    # ==========================================================

    if (
        "tempo ligado" in pergunta
        or "quanto tempo está ligado" in pergunta
        or "quanto tempo esta ligado" in pergunta
        or "uptime" in pergunta
    ):
        horas, minutos = sistema.uptime()
        return (
            f"Seu computador está ligado há "
            f"{horas} horas e {minutos} minutos. ⏱️"
        )

    # ==========================================================
    # ❓ AJUDA
    # ==========================================================

    if (
        pergunta == "ajuda"
        or "o que posso perguntar" in pergunta
        or "comandos" in pergunta
    ):
        return """
🤖 Eu sou a pAI! Você pode perguntar coisas como:

🧠 "Qual minha CPU?"
📊 "Quanto da CPU estou usando?"
🧮 "Quanta RAM eu tenho?"
📈 "Quanto de RAM estou usando?"
💾 "Quanto espaço livre eu tenho?"
🌡️ "Qual a temperatura da CPU?"
📋 "Quantos processos existem?"
🐧 "Qual meu sistema?"
⚙️ "Qual kernel?"
📦 "Qual minha arquitetura?"
⏱️ "Quanto tempo está ligado?"
🖥️ "Resumo do PC"

Ainda estou aprendendo! 🚀
"""

    # ==========================================================
    # 🤷 NÃO ENTENDIDO
    # ==========================================================

    return "Ainda não sei responder isso. 🤖"


# ==============================================================
# 🚀 INICIALIZAÇÃO
# ==============================================================

print("pAI 0.4.1 🤖")
print("Assistente local do Linux Mint 🐧")
print("Digite 'ajuda' para ver o que posso fazer.")
print("Digite 'sair' para fechar.\n")


while True:
    pergunta = input("Você: ")

    if pergunta.lower().strip() == "sair":
        print("pAI: Até mais! 🐧")
        break

    resposta = responder(pergunta)

    print("pAI:", resposta)
