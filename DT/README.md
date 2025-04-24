

# Exploring Youth Drug Use with Decision Trees

## Overview
This project analyzes factors influencing substance use among U.S. youth using data from the **2020 National Survey on Drug Use and Health (NSDUH)**. We use decision tree-based models to understand and predict behaviors related to alcohol and tobacco consumption.

## Objectives
The project aims to answer the following research questions:

1. **Binary Classification – Alcohol Use:**  
   Can we predict whether a youth has ever consumed alcohol based on parental, peer, and school influences?  
   _Target: `ALCFLAG`_

3. **Multi-class Classification – Level of Cigarette Use:**  
   Can we classify cigarette usage into low, medium, or high categories?  
   _Target: `IRCIGFM`_

4. **Regression – Cigarette Use Frequency:**  
   How many days per month does a youth smoke cigarettes?  
   _Target: `CIGMDAYS`_

## Dataset
- **Source:** [NSDUH 2020 Public Use File](https://www.samhsa.gov/data/data-we-collect/nsduh-national-survey-drug-use-and-health/datafiles/2020)
- **Filtered Sample:** Youths under age 18
- **Features:** Demographics, peer disapproval, parental monitoring, drug education, youth experiences, and more

## Methods
- **Models Used:**
  - Decision Tree
  - Random Forest (Bagging)
  - Gradient Boosting (Boosting)
- **Steps:**
  - Data Cleaning and Feature Selection
  - Train-Test Split (70/30)
  - Hyperparameter Tuning with GridSearchCV
  - Evaluation using accuracy (classification) and R², MAE, RMSE (regression)

## Results Summary
| Task                         | Best Model         | Key Metric            | Value     |
|------------------------------|--------------------|------------------------|-----------|
| Binary Classification (Alcohol) | Decision Tree       | Accuracy               | ~80%      |
| Binary Classification (Cigarettes) | Random Forest    | Accuracy               | ~81%      |
| Multi-class Classification   | Gradient Boosting  | Accuracy               | ~34.2%    |
| Regression (CIGMDAYS)        | Gradient Boosting  | R² Score               | ~0.02     |

## Key Takeaways
- Parental monitoring and peer disapproval are strong predictors.
- Ensemble models like Random Forest and Gradient Boosting improve accuracy.
- Predicting exact frequency of cigarette use remains difficult—may need more behavioral data.

## File Structure
```bash
├── youth_data.csv            # Cleaned dataset for youth under 18
├── NSDUH-2020-codebook.pdf   # Codebook for variable reference
├── DT.pptx                   # PowerPoint presentation
└── README.md                 # Project documentation
```

## Requirements
- Python 3.8+
- pandas, numpy
- scikit-learn
- matplotlib, seaborn (for visualization)
- Jupyter Notebook



## Author
**Suryakailash Ramesh**  
Graduate Student, Seattle University  
Email:
LinkedIn:
---

## Acknowledgments
- NSDUH Public Use Data Files – SAMHSA
```
