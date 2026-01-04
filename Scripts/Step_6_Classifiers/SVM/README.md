# 📘 SVM Parameters

This project provides a script to test different **Support Vector Machine (SVM)** configurations, evaluating multiple kernels and cross-validation, with automatic generation of **HTML reports**, charts, and statistical metrics.

---

## 📦 Requirements

- Python **3.8+**
- Linux / macOS (or WSL on Windows)

---

## 🚀 Installation and Configuration

### 1️⃣ Create virtual environment

```
python3 -m venv myenv
```

### 2️⃣ Activate the virtual environment

```
source myenv/bin/activate
```

### 3️⃣ Install dependencies
```
pip install libsvm
pip install brisque
pip install scikit-learn
pip install Jinja2
pip install matplotlib
pip install seaborn
```

# ▶️ Running the Script

After configuring the environment, run:

```
python svmParameters.py -dataset DATA.libsvm 
```

🔁 Replace **DATA.libsvm** with the name of your .libsvm file.

# SVM Model Parameters (LIBSVM)

| Parameter       | Symbol | Values used    | Description                                                               |
| --------------- | ------- | -------------- | ------------------------------------------------------------------------- |
| Kernel          | `-t`    | `0, 1, 2, 3`   | Kernel type:<br>0 = Linear<br>1 = Polynomial<br>2 = RBF<br>3 = Sigmoid    |
| Cost            | `-c`    | `10⁰, 10³`     | Penalization parameter (regularization)                                   |
| Gamma           | `-g`    | `10⁰`          | Kernel width parameter (RBF, Poly, Sigmoid)                               |
