# Week 4 Sprint Reflection

## Week 4 - Model Optimization and Generalization

During Week 4 of the 60 Days Coding Challenge, I focused on improving Machine Learning models and understanding how they perform on unseen data.

### What I Learned

I learned how different Machine Learning techniques can work together to create a more reliable ML workflow.

The main concepts I practiced were:

- Feature selection
- Feature engineering
- Model selection
- Cross-validation
- Hyperparameter tuning
- Bias and variance
- Model generalization
- ML pipelines

### Day 25 - Cross-Validation

I learned how cross-validation can be used to evaluate model performance across multiple data splits instead of depending on a single train-test split.

### Day 26 - Hyperparameter Tuning

I used hyperparameter tuning to search for better model configurations and understand how model settings can affect performance.

### Day 27 - Bias vs Variance

I compared training and validation performance using different Decision Tree complexity levels.

This helped me understand the difference between underfitting and overfitting and why model complexity matters.

### Day 28 - Optimized ML Pipeline

I combined preprocessing, validation, and hyperparameter tuning into a single Machine Learning pipeline.

The pipeline used:

- StandardScaler
- Random Forest Classifier
- Stratified 5-Fold Cross-Validation
- GridSearchCV

I then compared the original pipeline with the optimized pipeline using test accuracy.

### Engineering Tradeoffs

Optimization can improve model performance, but it may also require additional computation and training time.

Therefore, a production ML system should consider both performance and computational cost.

### Key Takeaway

Week 4 helped me understand that building a Machine Learning model is not only about training a model.

A reliable ML system also requires:

- Proper preprocessing
- Validation
- Feature preparation
- Model tuning
- Generalization analysis
- Reproducible workflows

This sprint helped me move from experimenting with individual ML techniques toward building a complete and reproducible ML workflow.