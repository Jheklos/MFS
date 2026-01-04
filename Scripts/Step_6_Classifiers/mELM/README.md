# 📘 ELM Parameters 

This project provides a script to test different **Extreme Learning Machine (ELM) configurations**, evaluating multiple kernels, number of neurons, and cross-validation, with automatic generation of **HTML reports**, charts, and statistical metrics.

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
pip install scikit-learn
pip install pandas
pip install Jinja2
pip install matplotlib
pip install seaborn
```

# ▶️ Running the Script

After configuring the environment, run:

```
python3 melmParameters.py \
  -tall DATA.csv \
  -ty 1 \
  -nh 50,200,1000 \
  -af sigmoid,linear,radbas \
  -sd 42 \
  -kfold 10 \
  -v
```

🔁 Replace **DATA.csv** with your CSV file name.


# 🧠 Algorithm Description

The script performs automated ELM tests by varying:

* Activation functions (kernels)
* Number of hidden neurons
* Cross-validation (k-fold)
* Random seed
* Generation of visual and statistical reports

# ⚙️ Parameters

| Parameter                   | Description                            |
| --------------------------- | -------------------------------------- |
| `-tall data.csv`            | Loads all data from the CSV file       |
| `-ty 1`                     | Target variable column                 |
| `-nh 50,100,200`            | Number of neurons to test              |
| `-af sigmoid,linear,radbas` | Activation functions (kernels / AFs)   |
| `-sd 42`                    | Random generator seed                  |
| `-kfold 10`                 | 10-fold cross-validation                |
| `-v`                        | Verbose mode                           |



✅ Features

✔ Executes multiple kernels (sigmoid, linear, radbas)
✔ Tests different numbers of neurons (50, 200, 1000)
✔ Creates an HTML report with tables, images, and matrices
✔ Calculates mean and standard deviation of metrics
✔ Converts confusion matrices to percentages
✔ Automatically saves charts
✔ Identifies the best and worst kernel
✔ Prints terminal summary in LaTeX-like format

📊 Calculated Metrics

* Train Rate (%)
* Test Rate (%)
* Train Time (s)
* Test Time (s)

🖥️ Generated Outputs

At the end of the execution:

✔ Terminal print of the best and worst kernel
✔ Confusion matrices (mean ± standard deviation) in percentage
✔ `elm_report.html` file
✔ `elm_report_images/` directory containing the charts

🧪 Using Other Kernels

⚠️ Warning: this command may require high computational cost.

```
python3 melmParameters.py \
  -tall data.csv \
  -ty 1 \
  -nh 50,200,1000 \
  -af sigmoid,linear,radbas,sin,hardlim,tribas,erosion,dilation,fuzzy-erosion,fuzzy-dilation \
  -sd 42 \
  -kfold 10 \
  -virusNorm \
  -v
```
