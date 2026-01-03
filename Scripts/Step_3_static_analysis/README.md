# Transformar em planilha

você precisa criar essa estrutura:

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

Para criar a estrutura dentro da pasta step_3_static_analysis rode o comando:
```
mkdir -p ../files_txt/APT/benign/analysis
mkdir -p ../files_txt/APT/malware/analysis

```

Coloque os arquivos .txt do pescanner dentro de (vai ser criado fora da pasta Step_3_static_analysis):

../files_txt/APT/benign/analysis/

../files_txt/APT/malware/analysis/

Dentro da pasta Step_3_static_analysis Rode o script principal:
```
python3 montar_planilhas.py                                       
```
Juntar os dois CSV em uma unica planilha com os dados balanceados exemplo: 1000 malware vs 1000 benign
