# Machine Learning for Food Processing Prediction.

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
1. **Data Collection:** Historical order data with timestamps, restaurant info, and menu details are collected from Kaggle  
2. **Preprocessing:** Handle missing values, encode categorical features, and normalize numeric ones  
3. **Modeling:** Train regression models (Linear Regression, Random Forest, XGBoost)  
4. **Evaluation:** Use metrics such as **MAE**, **RMSE**, and **R²** to compare with lookup-based baselines 
5. **Deployment:**  Package your model as a web service and deploy it with Docker

---

## ⚙️ Tech Stack  
- **Python**  
- **pandas**, **NumPy**, **scikit-learn**, **XGBoost**  
- **Matplotlib**, **Seaborn** for data visualization  
- **Jupyter Notebook** for experimentation  

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