# NYC-Taxis 
## Données utilisées

https://www.kaggle.com/c/nyc-taxi-trip-duration/data?select=train.zip

## Architecture du projet

```
.
├── data
│   ├── 01_raw
│   │   └── train.csv
│   └── 02_intermediate
│       ├── dirty_train.csv
│       └── train.csv
├── notebooks
│   ├── data_visualisation.ipynb
│   └── linear_regression.ipynb
├── src
│   ├── __init__.py
│   ├── data_cleaning.py
│   └── gpsutils.py
├── .gitignore
├── README.md
├── requirements.txt
└── Trello.png
```

- Data cleaning effectué dans `src/data_cleaning.py`
- Première partie du brief effectué dans `notebooks/data_visualisation.ipynb`
- Exercice additionnel effectué dans `notebooks/linear_regression.ipynb`

`src/gpsutils.py` : fonctions qui permet de calculer une distance avec coordonnées de départ et arrivée
`Trello.png` : screenshot du Trello du projet