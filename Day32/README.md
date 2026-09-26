# Create README file

readme_text = """
# Day 32 - Personalized Product Recommendation Engine

## Objective

Build a personalized product recommendation engine using
customer purchasing behavior and customer similarity.

## What I Built

- Customer-product purchase matrix
- Customer similarity analysis
- Similar customer identification
- Personalized product recommendations
- Recommendation relevance evaluation
- Recommendation score visualization
- Personalization strategy documentation

## Technique Used

### Cosine Similarity

Cosine similarity is used to compare customers based on
their product purchasing behavior.

## Recommendation Process

Customer Purchase Data
        ↓
Customer-Product Matrix
        ↓
Cosine Similarity
        ↓
Similar Customers
        ↓
New Products
        ↓
Personalized Recommendations

## Files

- `day32.ipynb` - Main notebook
- `similar_customer_analysis.csv` - Similar customer results
- `recommendation_output.csv` - Recommended products
- `recommendation_relevance.csv` - Relevance evaluation
- `recommendation_scores.png` - Recommendation visualization
- `recommendation_strategy.md` - Personalization strategy

## Key Learning

Customer similarity can be used to create personalized
product recommendations based on purchasing behavior.

## Tools

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
"""

with open("README.md", "w", encoding="utf-8") as file:
    file.write(readme_text)

print("README created successfully!")