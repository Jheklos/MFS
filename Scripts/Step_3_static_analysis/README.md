# Convert to CSV

You need to create this structure:

```
Step_3_static_analysis/
├── montar_planilhas.py
├── PegaDlls.py
├── PegaIAT.py
├── PegaResource.py
../
└── files_txt/
    └── APT/
        ├── benign/
        │   └── analysis/
        │       ├── benign1.txt
        │       └── benign2.txt
        └── malware/
            └── analysis/
                ├── malware1.txt
                └── malware2.txt

```

To create the structure inside the `step_3_static_analysis` folder, run the command:
```
mkdir -p ../files_txt/APT/benign/analysis
mkdir -p ../files_txt/APT/malware/analysis

```

Place the pescanner .txt files inside (it will be created outside the `Step_3_static_analysis` folder):

../files_txt/APT/benign/analysis/

../files_txt/APT/malware/analysis/

Inside the `Step_3_static_analysis` folder, run the main script:
```
python3 montar_planilhas.py                                
```
Merge the two CSVs into a single spreadsheet with balanced data, example: 1000 malware vs 1000 benign
