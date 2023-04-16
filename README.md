# Classifying Product from their Ingredients Based on various Machine Learning Algorithms.
## Team InsightScan 
### CSE523 - Machine Learning, Ahmedabad University 
## Introduction 
Our goal is to use machine learning techniques to accurately classify products as either food or beauty products based on their ingredient lists. To achieve this, we gathered data by manually collecting ingredient information from 1100 food and beauty products using the ChatGPT API, resulting in a total of 1672 unique ingredients. We conducted pre-processing on the data and tested various classification algorithms. Based on the results, we developed ensemble learning models that were fine-tuned for optimal test performance. We utilized Support Vector Machine (SVM) as the most suitable model for our dataset, and implemented additional techniques such as PCA, GridSearchCV, and Cosine similarity to improve results. We also created a recommendation model that would give a list of similar products based on the given input product from our dataset.

## Results 
For comparison of all the results generated by different algorithms, check the table in the [report](https://github.com/aharnishp/InsightScan-ML/blob/master/Report/7_InsightScan_End_Sem_Project_Report.pdf).

### Classification

#### Cumulative Explained Varience vs No. of Components
![cumulative_explained_varience](https://user-images.githubusercontent.com/63735761/232238240-0854d702-630e-4b6e-b5ac-6adac2e24b43.jpg)

#### ROC Curve
![precision_recall_curve](https://user-images.githubusercontent.com/63735761/232238556-4e539208-451b-4047-96cc-106c0ac64058.jpg)

#### Precision Recall Curve
![recall_curve](https://user-images.githubusercontent.com/63735761/232238611-105be039-8c36-4043-8a80-85163eacce2a.jpg)

#### Data Visualization after PCA with 2D
![data_visulization_after_pca_with_2_dimentions](https://user-images.githubusercontent.com/63735761/232238633-fe3197ad-d09e-4a04-90b7-f9e11eeb9118.jpg)

#### Heat Map After PCA
![heat_map_after_pca](https://user-images.githubusercontent.com/63735761/232238678-69a03ad0-c8f0-41c3-a85c-3551ce9f7cc1.jpg)

#### Poster
![poster](https://user-images.githubusercontent.com/63735761/232242066-11a328e1-34b8-4f1b-9dae-eb2faaeed6cc.png)

## References
* Swain, P. H., & Hauska, H. (1977). The decision tree classifier: Design and potential. IEEE Transactions on Geoscience Electronics, 15(3), 142-147.
* Hosmer Jr, D. W., Lemeshow, S., & Sturdivant, R. X. (2013). Applied logistic regression (Vol. 398). John Wiley & Sons.
* Dasu, T., & Johnson, T. (2003). Exploratory data mining and data cleaning. John Wiley & Sons.
* Pal, M. (2005). Random forest classifier for remote sensing classification. International journal of remote sensing, 26(1), 217-222.
* F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas,
A. Passos, D. Cournapeau, M. Brucher, M. Perrot, and E. Duchesnay, “Scikit-learn: Machine learning in Python,” Journal of Machine Learning Research, vol. 12, pp. 2825–2830, 2011.
