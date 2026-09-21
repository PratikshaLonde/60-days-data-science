# Day 27 - Bias vs Variance in ML Systems

## Understanding Bias vs Variance in ML Systems

### Objective

Understand how model complexity affects training and validation performance and analyze the bias-variance tradeoff in a Machine Learning system.

### Tasks Completed

* Compared training and validation performance
* Used Decision Tree models with different complexity levels
* Adjusted `max_depth` to study model complexity
* Identified potential underfitting and overfitting patterns
* Calculated the training-validation accuracy gap
* Created a learning curve using 5-Fold Cross-Validation
* Visualized training and validation behavior
* Documented generalization observations

### Model

**Decision Tree Classifier**

### Model Complexity

Different `max_depth` values were tested:

* 1
* 2
* 3
* 5
* 10
* 15
* None

### Analysis

Training accuracy shows how well the model fits the training data, while validation accuracy shows how well the model performs on unseen data.

A large difference between training and validation performance can indicate overfitting or high variance. Low performance on both can indicate underfitting or high bias.

The analysis uses actual validation results from the experiment rather than assuming that a particular model depth is always optimal.

### Learning Curve

A learning curve was created to observe how training and validation performance change as more training data is used.

### Files

* `day27.ipynb` - Bias-variance analysis notebook
* `bias_variance_analysis.csv` - Training, validation, and accuracy-gap results
* `bias_variance_accuracy.png` - Training vs validation accuracy visualization
* `learning_curve.png` - Learning curve visualization

### Key Learning

The bias-variance tradeoff is an important part of Machine Learning generalization.

A model that is too simple may underfit the data, while a model that is too complex may overfit the training data. Comparing training and validation performance helps identify these behaviors and understand how model complexity affects generalization.

### Conclusion

Day 27 demonstrated how changing Decision Tree complexity affects model performance and how learning curves and validation results can be used to study generalization and the bias-variance tradeoff.
