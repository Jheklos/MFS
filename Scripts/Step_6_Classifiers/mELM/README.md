# 📘 ELM Parameters 

Este projeto fornece um script para testar diferentes **configurações de Extreme Learning Machine (ELM)**, avaliando múltiplos kernels, números de neurônios e validação cruzada, com geração automática de **relatórios HTML**, gráficos e métricas estatísticas.

---

## 📦 Requisitos

- Python **3.8+**
- Linux / macOS (ou WSL no Windows)

---

## 🚀 Instalação e Configuração

### 1️⃣ Criar ambiente virtual

```
python3 -m venv myenv
```

### 2️⃣ Ativar o ambiente virtual


```
source myenv/bin/activate

```

### 3️⃣ Instalar dependências
```
pip install scikit-learn
pip install pandas
pip install Jinja2
pip install matplotlib
pip install seaborn
```

# ▶️ Executando o Script

Após configurar o ambiente, execute:

```
python3 melmParameters.py \
  -tall DADOS.csv \
  -ty 1 \
  -nh 50,200,1000 \
  -af sigmoid,linear,radbas \
  -sd 42 \
  -kfold 10 \
  -v
```

🔁 Substitua **DADOS.csv** pelo nome do seu arquivo CSV.


# 🧠 Descrição do Algoritmo

O script executa testes automatizados de ELM variando:

* Funções de ativação (kernels)

* Número de neurônios ocultos

* Validação cruzada (k-fold)

* Seed aleatória

* Geração de relatórios visuais e estatísticos

# ⚙️ Parâmetros


| Parâmetro                   | Descrição                             |
| --------------------------- | ------------------------------------- |
| `-tall dados.csv`           | Carrega todos os dados do arquivo CSV |
| `-ty 1`                     | Coluna da variável alvo               |
| `-nh 50,100,200`            | Quantidades de neurônios a testar     |
| `-af sigmoid,linear,radbas` | Funções de ativação (kernels / AFs)   |
| `-sd 42`                    | Seed do gerador aleatório             |
| `-kfold 10`                 | Validação cruzada 10-fold             |
| `-v`                        | Modo verbose                          |



✅ Funcionalidades

✔ Executa múltiplos kernels (sigmoid, linear, radbas)

✔ Testa diferentes números de neurônios (50, 200, 1000)

✔ Cria relatório HTML com tabelas, imagens e matrizes

✔ Calcula média e desvio padrão das métricas

✔ Converte matrizes de confusão para porcentagem

✔ Salva gráficos automaticamente

✔ Identifica melhor e pior kernel

✔ Imprime resumo no terminal em formato LaTeX-like

📊 Métricas Calculadas

* Train Rate (%)

* Test Rate (%)

* Train Time (s)

* Test Time (s)

🖥️ Saídas Geradas

Ao final da execução:

✔  Impressão no terminal do melhor e pior kernel

✔  Matrizes de confusão (média ± desvio padrão) em porcentagem

✔ Arquivo elm_report.html

✔  Diretório elm_report_images/ contendo os gráficos

🧪 Utilizando Outros Kernels

⚠️ Atenção: este comando pode demandar alto custo computacional.

```
python3 melmParameters.py \
  -tall dados.csv \
  -ty 1 \
  -nh 50,200,1000 \
  -af sigmoid,linear,radbas,sin,hardlim,tribas,erosion,dilation,fuzzy-erosion,fuzzy-dilation \
  -sd 42 \
  -kfold 10 \
  -virusNorm \
  -v
```
