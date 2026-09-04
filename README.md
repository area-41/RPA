# Automatização de tarefas (RPA) usando Python


### RPA - Robotic Process Automation Portfolio & Modules
🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖

Uma coleção de módulos, scripts e automações focadas em **Robotic Process Automation (RPA)** e extração de dados utilizando ecossistema Python. Desde web scraping e navegação automatizada até automação de interface de usuário (GUI) e extração de dados via OCR (Reconhecimento Óptico de Caracteres).


## Estrutura do Repositório

```text
RPA/
├── 1_extrator_pdf/             # Módulo de extração e processamento de documentos PDF
├── 2_monitor_cesta_basica/     # Aplicação/monitor de dados (src) para monitoramento de preços
├── 3_webscraping/              # Scripts de scraping estático e parsing de páginas web
├── 4_selenium/                 # Automações web baseadas em Selenium WebDriver
├── 5_pyautogui/               # Automação de interface desktop, cliques e teclado (GUI Automation)
├── 6_tesseract_ocr/            # Processamento de imagens e extração de texto via Tesseract OCR
│
├── main.py                     
├── show_info_project.py        # Script auxiliar para exibição de métricas e status do projeto
├── dados_livros.xlsx           # Planilha de dados exportados/gerados pelos módulos
│
├── pyproject.toml              # Configuração do projeto e dependências 
├── uv.lock                     # Lockfile para reproduzibilidade de ambiente via uv
├── .python-version             
├── tamanho_dependencias.txt    # Relatório de footprint e consumo de dependências
├── .gitignore                  
└── LICENSE                     

```

## Tecnologias e Ferramentas Utilizadas

* **Linguagem:** Python 3.x
* **Gerenciamento de Pacotes e Ambientes:** [`uv`](https://github.com/astral-sh/uv)
* **Automação Web & Scraping:** Selenium, BeautifulSoup / Requests
* **Automação Desktop:** PyAutoGUI
* **Visão Computacional & OCR:** Tesseract OCR, Pillow / OpenCV
* **Manipulação de Dados:** Pandas, OpenPyXL


## Pré-requisitos e Instalação

O projeto utiliza o **`uv`** como gerenciador de dependências e ambientes virtuais para garantir alta performance e instalação rápida.

### 1. Clonar o repositório

```bash
git clone [https://github.com/area-41/RPA.git](https://github.com/area-41/RPA.git)
cd RPA

```

### 2. Sincronizar o ambiente com o `uv`

Se você já possui o `uv` instalado, execute o comando abaixo para criar o ambiente virtual (`.venv`) e instalar automaticamente todas as dependências fixadas no `uv.lock`:

```bash
uv sync

```

*(Caso não utilize o `uv`, você pode criar um ambiente virtual tradicional com `python -m venv .venv` e instalar os pacotes via `pip` baseando-se no `pyproject.toml`).*


## Como Executar

### Execução Principal

Para rodar o ponto de entrada principal do projeto:

```bash
uv run main.py

```

### Informações do Projeto

Para visualizar relatórios de status ou metadados das automações:

```bash
uv run show_info_project.py

```

### Executar Módulos Individuais

Cada diretório numérico contém casos de uso específicos. Para testar um script individual de automação (exemplo: Selenium):

```bash
uv run 4_selenium/iniciando_navegacao.py

```


## Módulos do Projeto

| Módulo | Descrição / Caso de Uso |
| --- | --- |
| **`1_extrator_pdf`** | Leitura estruturada, extração de texto e tabelas contidas em arquivos PDF. |
| **`2_monitor_cesta_basica`** | Coleta automatizada e monitoramento histórico do custo de itens de cesta básica. |
| **`3_webscraping`** | Requisições HTTP e parsing HTML para extração de dados públicos web. |
| **`4_selenium`** | Navegação autônoma em navegadores para interação com formulários e dashboards complexos. |
| **`5_pyautogui`** | Interações diretas com elementos visuais da tela, teclado e mouse para aplicações legadas. |
| **`6_tesseract_ocr`** | Digitalização e reconhecimento óptico de caracteres em documentos e imagens. |

---

## Licença

Este projeto está licenciado sob os termos da licença constante no arquivo [LICENSE](https://www.google.com/search?q=LICENSE).

Agradecimentos à professora Natássya Silva.