# Project Log for Tabular Playground Series Jan-21

This file includes workday notes on major steps taken, findings / analytical insights, and reflections on learning from the exercise. I intend it to document my working progress and promote critical reflection on the coding I complete.



### Day 1

**Goal:** Initial EDA of the provided dataset.


**Major Observations:**
1. Clean dataset has no missing values
2. Features values almost perfectly on [0,1] suggesting some pre-standardization
3. Most features display minimal relationship to the target
4. Some features exhibit major clustering within dense regions of the support
5. Even those features with the highest pairwise correlation have extremely high variance in values around that relationship.


**Implications:**
1. The high variance and weak relationships to target will limit the peak accuracy of any predictive model
2. Significant feature restructuring such as binning should be explored
3. The lack of labels prevents any intuition from domain knowledge

**Reflection** <br>
The lack of domain-based intuition reduces this challenge to a purely score-based model building practice. The lack of labelling prevents any research into the underlying data generation process and prevents any initial intuition about the form the predictive model should take. This likely results from a synthetic data generation process.

As an entry-level targeted challenge, this may simplify the exercise to the coding of data transformations and model testing. However, I find this risks leading early aspiring data scientists into bad habits. Domain knowledge should inform every step of the modeling process. A good data scientist should occasionally step back and ask if his or her findings make intuitive sense and reflect reality to prevent future errors.



### Day 2

**Goals:** Further EDA of the provided dataset, Widgets for visuals


**Major Observations:**
1. Most feature pairs display very weak correlation patterns visually.
2. Successfully implemented additional ipywidgets within notebook.


**Reflection** <br>
The focus on implementing new widgets to control space for visual plots limited the amount of additional EDA completed today. Stack Overflow Q&As found from google searches proved extremely fruitful for providing templates of widgets to adapt to my purpose. Incorporating these structures into future analysis the first time through will save significant time and be a provide a useful reference.



### Day 3

**Goal:** Begin Feature Engineering and EDA


**Major Observations:**
1. Power transformation of provided features had few positive impacts
2. Interaction features exhibited much stronger correlations than pure features
3. Simple baselines had high RMSE scores


**Implications:**
1. Interaction terms should improve model performance by capturing more complex relationships between provided features and the target.
2. Further motivates desire to compare base models to PCR.


**Reflection** <br>
After creating an OLS and Ridge baseline, I confirmed these base models on original features perform poorly in an absolute sense. However, viewing the Kaggle leaderboard reveals even the top performing submissions only outperform these simple baselines by only about 0.03 RMSE points. The high variance in the data and weak relationships to the target create great difficulty in creating a high-performing model.

The initial exploration of interaction terms suggest incorporating these features or principal components should improve my baseline performance.



### Day 4

**Goal:** Baseline Models and Feature Engineering


**Major Observations:**
1. In the OLS model with 3rd degree polynomial features, most bivariate interaction terms and solo features are statistically significant at the 95% confidence level.
2. After generating new additive and ratio variables, few exhibit stronger correlation to the target than the original features.


**Implications:**
1. Even engineered features provide minimal information about the target variable. Thus no models have outperformed a naive train average by more than a few percentage points.


**Reflection** <br>
The provided and easily derived features provide minimal predictive power. The direction of my analysis moving forward will be on utilizing local neighbors to predict the target. The large number of observations makes k-nearest neighbors infeasible. I intend to explore utilizing clustering approaches to identify clusters to use as categorical features in other models and improve the overall average baseline.



### Day 5

**Goal:** Explore cluster averages, cluster features, and KNN


**Major Observations:**
1. K-means cluster averages do not outperform overall target average.
2. K-means clusters in feature space do no correlate with target value.
3. Incorporating K-means clusters into linear models does not improve performance.
4. K Nearest Neighbors Regressor performs reasonably well on training data but still suffers poor performance on test data.


**Implications:**
1. Identifying meaningful clusters in feature space does not improve predictive performance.
2. The high-variance of target values dominates the very weak relationships to any features.


**Reflection** <br>
The failure of cluster-feature methods was very disappointing. Perhaps this should have been expected due to the lack of relationship between features and the target. Revisiting the visualizations of features in the exploratory notebook, many features had high density subregions within the domain but the target had no systematic relationship to these subregions. The targets displayed high variance in values across each domain.


Next, I'm going to explore binning the target variable into over or under average and create categorical predictive models. The target displays a bimodal distribution. Identifying which dense region an observation belongs to should dramatically improve performance.



### Current Submissions

| Model           | Notes          | Public Leaderboard | Improvement |
|-----------------|----------------|--------------------|-------------|
| OLS             | Poly2 Features | 0.71682            | -           |
| OLS + Clusters  | k=9            | 0.72048            | No          |
| K-Means Average | k=9            | 0.72997            | No          |
| K-Means Average | k=20           | 0.72819            | No          |
| KNN Regressor   | n=111          | 0.71434            | Yes         |
