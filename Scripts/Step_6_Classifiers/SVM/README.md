# 📘 SVM Parameters 

Este projeto fornece um script para testar diferentes **configurações de Support Vector Machine (SVM)**, avaliando múltiplos kernels, e validação cruzada, com geração automática de **relatórios HTML**, gráficos e métricas estatísticas.

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
pip install libsvm
pip install brisque
pip install scikit-learn
pip install Jinja2
pip install matplotlib
pip install seaborn
```
# ▶️ Executando o Script

Após configurar o ambiente, execute:

```
python svmParameters.py -dataset DATA.libsvm 

```

🔁 Substitua **DATA.libsvm** pelo nome do seu arquivo .libsvm 

#Parâmetros do modelo SVM (LIBSVM)


| Parâmetro       | Símbolo | Valores usados | Descrição                                                                 |
| --------------- | ------- | -------------- | ------------------------------------------------------------------------- |
| Kernel          | `-t`    | `0, 1, 2, 3`   | Tipo de kernel:<br>0 = Linear<br>1 = Polinomial<br>2 = RBF<br>3 = Sigmoid |
| Custo           | `-c`    | `10⁰, 10³`     | Parâmetro de penalização (regularização)                                  |
| Gamma           | `-g`    | `10⁰`          | Parâmetro de largura do kernel (RBF, Poly, Sigmoid)                       |
