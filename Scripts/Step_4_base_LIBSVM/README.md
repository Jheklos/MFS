# Converter planilha para  .libsvm 


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

### 3️⃣ Instalar dependências caso necessário
```
pip install DEPENDENCIA

```
🔁 Substitua **DEPENDENCIA** pelo nome da dependência necessária

## Colocar  o csv na mesma pasta do script

# ▶️ Executando o Script

Após configurar o ambiente, execute:

```
python converter_libsvm.py DATA.csv DATA.libsvm


```

🔁 Substitua **DATA.csv** pelo nome do seu arquivo CSV e crie o nome do .libsvm



ou com o caminho
```
python converter_libsvm.py /caminho/para/DATA.csv /caminho/para/DaTA.libsvm

```


# Facultativo (não foi utilizado no artigo de persquisa) :


```
python3 preprocess_and_split_space.py Data.csv

```

Isso vai gerar:

* Data_train.txt

* Data_test.txt

Ambos compatíveis diretamente com o melm.py onde podera rodar o código:

```

python3 melm.py -tr Data_train.txt -ts Data_test.txt -ty 1 -nh 100 -af sigmoid -v
```
