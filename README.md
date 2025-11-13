# Machine Learning for Food Processing Time Prediction.

##  Project Overview  
This project predicts **food processing time** — the duration between when an order is placed and when it is ready — for a **food delivery app**.  
Accurate estimates help improve **customer satisfaction**, **restaurant efficiency**, and **delivery planning**.


##  Problem Statement  
Food preparation time can vary based on **restaurant workload**, **order size**, **dish type**, and **time of day**.  
Most delivery systems rely on static or rule-based lookups that fail to adapt to real-world dynamics.  
This project uses **machine learning** to build a **data-driven model** that provides more reliable and adaptive processing time estimates.


## Objectives  
- Develop an ML model to predict food processing time  
- Identify key drivers influencing preparation duration  
- Compare model performance with a simple lookup baseline  
- Improve ETA (Estimated Time of Arrival) predictions for customers  


##  Methodology  
1. **Data Collection:** Historical order data with day of the week, restaurant name, and cuisine and cost details, are collected from Kaggle.  
2. **Preprocessing:** Only the ratings column had missing values and this was dropped. Considering the high sparsity of the order_id and customer_id, a hashing feature was considered. For categorical features, one hot encoding was utilized to convert to numerical features. The cost of order, which was scaled using the standard scaler. This makes the numerical features to be in comparable range. Although scaling wasn't required for tree-based models explored, since linear models were explored, this scaling was done. All preprocessing and modelling (discussed in 3.) were packaged in a pipeline for ease of deployment and to avoid training/serving skew.
3. **Modeling:** Mutual information was explored to see what features were provide the most information about the target variable (i.e. food_preparation_time). It was discovered that the restaurant name gave the highest mutual information in a categorial feature -> categorical target scenario. In addition, the target variable distribution was somewhat uniform with preparation times within a small range (20- 35 minutes). This prompted me to explore a classification approach instead of regression. I did this by binning the targets into long, short and medium, then performing multiclass classification using Logistic Regression, Random Forest and XGBoost. The best performance was about 34% accuracy which wasn't much better than a baseline of 33% when randomly picking one of the targets. I then switched to a regression approach and achieve mean absolute error of about 4 minutes. This was fair. I tried post processing my classification above (i.e from long, short, medium to actual minutes e.g. 20, 25, 35 minutes). The MAE after postprocessing was about MAE of 7 minutes, which means that the regression approach achieved better performance. Thus, the random forest model which performed best was proceeded to hyperparamter tuning, and I was able to get an MAE of less than 4 minutes. In addition, for a single prediction, my model achieved a prediction within 1 minute of the ground truth. Considering the limitation of overall small mutual information between the features and the target label, I was still able to get the model to work. 
4. **Evaluation:** I used metrics such as **MAE**, **Accuracy** for evaluation in the regression and classification approaches respectively. Accuracy was sufficient because there was no severe class imbalance. 
5. **Deployment:**  I packaged my model as a web service using FastAPI and deployed it with Docker
6. **Design Patterns:**  I have read the book [*Machine Learning Design Patterns*](https://www.oreilly.com/library/view/machine-learning-design/9781098115777/), and I explored the following design patterns for this project:
- Design Pattern 1: Hashed Feature => Necessary to hash the high cardinality of the order_id and customer_id. Also helps to resolve the cold start issue with ids which are not seen during training.
- Design Pattern 5: Reframing =>  I explored this problem representation design pattern to see which approach was suitable for the problem. I explored the regression and classification approaches and found the regression approach to be more suitable.
- Design Pattern 15: Hyperparameter Tuning => I explored hyperparameter tuning to get the best performance with my RandomForect regression using the randomizedCV search. I was able to get the MAE to less than 4 minutes.
- Design Pattern 17: Batch Serving => I made a batch serving prediction using my pipeline.
- Design Pattern 22: Repeatable Splitting => To ensure that each (repeated)label was found in the training, val and test data splits, I stratified on the label. In addition, I set a random state to ensure that the split was repeatatble. 
- Design Pattern 25: Workflow Pipeline => As stated earlier, I package my processes in a pipeline to ensure no training and serving skew. Although the pipeline here is not as sophisticated as the workflow pipelines like Airflow stated in the book, my pipeline is also necessary and makes packaging the model easier.
7.  **Best Practices:**  I added the following to make the code compact and follow best industry practices
- Isort to sort my imports
- Black to format my code
- Precommit hooks to run isort and black and ensure my code is well formatted before committing

---

## ⚙️ Tech Stack  
- **Python**  
- **pandas**, **NumPy**, **scikit-learn**, **XGBoost**  
- **Matplotlib**, for data visualization  
- **Jupyter Notebook** for experimentation
- **FastAPI** as web service app 
- **uv** as dependency manager 

---

## 📊 Expected Outcome  
A predictive model that adapts to changing restaurant and order dynamics, outperforming rule-based estimates in predicting food preparation time and improving delivery ETA accuracy.


<!-- ## 🚀 Future Improvements  
- Integrate real-time API predictions into the delivery app  
- Include external factors like **traffic** and **weather**  
- Experiment with **deep learning** for multi-restaurant generalization   -->



### This project is a midterm project for DataTalks Club ML Engineering Zoomcamp
Requirements are 
1. Pick a problem that interests you and find a dataset
2. Describe the problem and how ML can help
3. Prepare the data and run EDA
4. Train several models, tune them, and pick the best
5. Export your notebook to a script
Package your model as a web service and deploy it with Docker