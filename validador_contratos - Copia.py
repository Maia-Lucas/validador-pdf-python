import re
import requests
import pdfplumber
from io import BytesIO


def baixar_pdf(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return r.content


def extrair_texto(pdf_bytes):
    texto = ""
    with pdfplumber.open(BytesIO(pdf_bytes)) as pdf:
        for p in pdf.pages:
            t = p.extract_text()
            if t:
                texto += t + "\n"
    return texto.upper()


def contar_linhas_parcela(texto):
    pattern = r"^PARCELA\S*\s+.*R\$\s*[0-9]"
    return len(re.findall(pattern, texto, flags=re.MULTILINE))


def extrair_numero_contrato(texto):
    padroes = [
        r"NÚMERO\s*[:\-]?\s*(\d+)"
    ]
    for p in padroes:
        m = re.search(p, texto)
        if m:
            return m.group(1)
    return "NÃO ENCONTRADO"


# lista para armazenar em memória também
sem_progressao = []

with open("links.txt", encoding="utf-8") as f:
    links = [l.strip() for l in f.readlines() if l.strip()]

total = len(links)
processados = 0

# abre o arquivo já no modo append
arquivo = open("resultado.txt", "a", encoding="utf-8")

for link in links:
    processados += 1
    try:
        print(f"[{processados}/{total}] Verificando: {link}")

        pdf_bytes = baixar_pdf(link)
        texto = extrair_texto(pdf_bytes)

        linhas = contar_linhas_parcela(texto)

        if linhas == 1:
            numero = extrair_numero_contrato(texto)
            sem_progressao.append((numero, link))

            # imprime imediatamente
            print(f"❌ SEM PROGRESSÃO -> {numero} -> {link}")

            # salva imediatamente
            arquivo.write(f"{numero} -> {link}\n")
            arquivo.flush()   # força gravar no disco na hora

    except Exception as e:
        print(f"Erro no link: {link} -> {e}")

arquivo.close()

print("\nFINALIZADO.")
print(f"Total sem progressão encontrados: {len(sem_progressao)}")

input("\nPressione ENTER para sair...")
