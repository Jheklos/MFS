# Convert Spreadsheet to .libsvm

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

### 3️⃣ Install dependencies if necessary

```
pip install DEPENDENCY
```
🔁 Replace **DEPENDENCY** with the name of the required dependency.

## Place the CSV in the same folder as the script

# ▶️ Running the Script

After configuring the environment, run:

```
python converter_libsvm.py DATA.csv DATA.libsvm
```

🔁 Replace **DATA.csv** with your CSV file name and create the name for the **.libsvm** file.

Or using the full path:

```
python converter_libsvm.py /path/to/DATA.csv /path/to/DATA.libsvm
```

# Optional (not used in the research paper):

```
python3 preprocess_and_split_space.py Data.csv
```

This will generate:

* Data_train.txt
* Data_test.txt

Both are directly compatible with `melm.py`, where you can run the code:

```
python3 melm.py -tr Data_train.txt -ts Data_test.txt -ty 1 -nh 100 -af sigmoid -v
```
