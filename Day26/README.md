# Day 26 - Hyperparameter Tuning

## Optimizing ML Systems with Hyperparameter Tuning

### Objective

Improve machine learning model performance by systematically searching for better hyperparameter combinations.

### Tasks Completed

- Selected Random Forest as the model for optimization
- Created an untuned Random Forest baseline
- Defined a hyperparameter search grid
- Applied GridSearchCV with 5-fold cross-validation
- Tuned key Random Forest hyperparameters
- Identified the best hyperparameter combination
- Compared untuned and tuned model performance
- Calculated the change in test accuracy
- Saved the best parameter report
- Created a performance comparison visualization
- Documented the optimization process

### Model

**Random Forest Classifier**

### Hyperparameters Tuned

- `n_estimators`
- `max_depth`
- `min_samples_split`
- `min_samples_leaf`

### Validation Method

GridSearchCV with 5-fold cross-validation was used to evaluate different hyperparameter combinations.

### Files

- `day26.ipynb` - Hyperparameter tuning notebook
- `best_parameters.csv` - Best hyperparameters found by GridSearchCV
- `hyperparameter_tuning_comparison.csv` - Untuned vs tuned performance comparison
- `hyperparameter_tuning_comparison.png` - Performance comparison visualization

### Key Learning

Hyperparameter tuning provides a systematic way to search for better model configurations instead of relying only on default settings.

GridSearchCV evaluates multiple combinations using cross-validation, helping identify promising parameter settings while reducing the risk of selecting a configuration based on a single data split.

### Optimization Trade-off

Hyperparameter tuning can improve model performance, but searching through more combinations increases computational cost. The goal is to find a useful balance between model performance, stability, complexity, and computation time.

### Conclusion

Day 26 demonstrated how hyperparameter tuning can be used to optimize a machine learning model systematically and compare the resulting model with an untuned baseline.