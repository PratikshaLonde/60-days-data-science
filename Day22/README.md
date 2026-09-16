# Day 22 - Feature Encoding

## Turning Raw Categories into Machine Learning Signals

### Objective

Transform categorical variables into numerical representations that machine learning models can understand.

### Tasks Completed

* Identified categorical columns
* Applied Label Encoding to the `category` column
* Applied One-Hot Encoding to the `segment` column
* Compared dataset structure before and after encoding
* Trained a Logistic Regression baseline model
* Compared model performance before and after encoding
* Saved the encoded dataset and performance comparison

### Encoding Techniques

**Label Encoding:**
Converts categories into numerical labels.

**One-Hot Encoding:**
Creates separate columns for each category.

### Model

Logistic Regression was used as the baseline classification model.

### Files

* `day22.ipynb` - Feature encoding notebook
* `encoded_dataset.csv` - Encoded dataset
* `encoding_performance_comparison.csv` - Model performance comparison
* `encoding_performance_comparison.png` - Accuracy comparison graph

### Key Learning

Feature encoding converts categorical information into numerical signals, allowing machine learning algorithms to process categorical data effectively.
