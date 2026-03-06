# 🛡️ Cyber Risk Dashboard

Dashboard interactif d'analyse de risques cybersécurité avec calcul de l'ALE (Annual Loss Expectancy) et du ROI des mesures de sécurité.

## 📋 Fonctionnalités

- **Analyse de risque unique** : Calcul de l'ALE (SLE × ARO)
- **Calcul du ROI** : Évaluation de la rentabilité des mesures de sécurité
- **Gestion multi-risques** : Priorisation de plusieurs risques simultanément
- **Visualisations interactives** : Graphiques dynamiques avec Plotly
- **Exemples pré-configurés** : Scénarios de risques courants (Ransomware, DDoS, Phishing...)

## Installation

### Prérequis
- Python 3.8 ou supérieur
- pip

### Installation des dépendances

```bash
pip install -r requirements.txt
```

## Utilisation

### Lancer l'application en local

```bash
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur à l'adresse `http://localhost:8501`

## Méthodologie

### Formules utilisées

**ALE (Annual Loss Expectancy)**
```
ALE = SLE × ARO
```

**SLE (Single Loss Expectancy)**
```
SLE = Valeur de l'actif × Facteur d'exposition (%)
```

**ROI (Return On Investment)**
```
ROI = ((Réduction du risque - Coût de la mesure) / Coût de la mesure) × 100
```

### Niveaux de risque

| ALE | Niveau | Couleur |
|-----|--------|---------|
| > 100 000€ | 🔴 CRITIQUE | Rouge |
| 50 000€ - 100 000€ | 🟠 ÉLEVÉ | Orange |
| 20 000€ - 50 000€ | 🟡 MOYEN | Jaune |
| < 20 000€ | 🟢 FAIBLE | Vert |

## Architecture

```
cyber-risk-dashboard/
│
├── app.py                 # Application Streamlit principale
├── requirements.txt       # Dépendances Python
├── README.md             # Documentation
└── .gitignore            # Fichiers à ignorer par Git
```

## Technologies utilisées

- **Python 3.x**
- **Streamlit** : Framework pour créer l'interface web
- **Pandas** : Manipulation de données
- **Plotly** : Visualisations interactives

## Références

- [ISO/IEC 27005](https://www.iso.org/standard/75281.html) : Gestion des risques en sécurité de l'information
- [NIST SP 800-30](https://csrc.nist.gov/publications/detail/sp/800-30/rev-1/final) : Guide for Conducting Risk Assessments
- [EBIOS Risk Manager](https://www.ssi.gouv.fr/ebios) : Méthode française d'analyse des risques

## Auteur

**acdv5**

## Licence

Ce projet est open source et disponible sous licence MIT.

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Forker le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

