# Validador de PDFs de Contratos em Python

Este projeto realiza a validação de contratos em PDF a partir de uma lista de links.
O script identifica contratos **com apenas uma linha de parcela (sem progressão)** e registra essas ocorrências em um arquivo de resultado.

Ele foi desenvolvido para automatizar conferências de contratos que seriam demoradas de validar manualmente.

## 🚀 Funcionalidades

- baixa PDFs a partir de URLs
- extrai o texto dos PDFs
- converte todo texto para maiúsculo (normalização)
- conta linhas relacionadas a parcelas
- identifica casos com **apenas 1 parcela**
- extrai o número do contrato
- mostra o progresso no terminal
- salva automaticamente os resultados em arquivo

## 🧰 Tecnologias utilizadas

- Python 3.13
- requests
- pdfplumber
- re (expressões regulares)
- io.BytesIO

## 📂 Estrutura esperada de arquivos

/seu-projeto  
 ├─ validador_pdf.py  
 ├─ links.txt  
 └─ resultado.txt  (gerado automaticamente)

## 📥 Entrada do sistema

O arquivo `links.txt` deve conter um link por linha, cada um apontando para um PDF válido.

Exemplo:
https://site.com/contrato1.pdf  
https://site.com/contrato2.pdf  
https://site.com/contrato3.pdf  

## 📤 Saída do sistema

O arquivo `resultado.txt` conterá linhas no formato:

NUMERO_DO_CONTRATO -> LINK_DO_PDF

Somente contratos detectados **sem progressão** são salvos.

## 🔧 Instalação e uso

1) Clonar o repositório  
git clone https://github.com/seu-usuario/seu-repositorio.git  

2) Entrar na pasta  
cd seu-repositorio  

3) Instalar dependências  
pip install -r requirements.txt  

4) Criar o arquivo `links.txt` com os links dos PDFs  

5) Executar o script  
python validador_pdf.py  

## 🧠 Lógica principal utilizada

O script:
1. baixa o PDF por HTTP  
2. converte o PDF em texto  
3. procura linhas começando por “PARCELA”  
4. conta essas ocorrências  
5. se encontrar **apenas uma**, considera “sem progressão”  
6. extrai o número do contrato  
7. grava a informação no arquivo de resultado  

## ⚠️ Observações importantes

- PDFs escaneados como imagem podem não funcionar  
- PDFs que bloqueiam extração de texto podem falhar  
- links inválidos são exibidos como erro no terminal  
- o script mantém um arquivo de saída incremental (append)

## ✔️ Exemplo de execução

[10/150] Verificando: https://site.com/contrato.pdf  
❌ SEM PROGRESSÃO -> 123456789 -> https://site.com/contrato.pdf  

FINALIZADO.  
Total sem progressão encontrados: 37  

## 🧾 Licença

Projeto livre para uso e modificação.

## 🤝 Contribuições

Sugestões e melhorias são bem-vindas! Abra uma issue ou envie um pull request.
