# Improving-Analytics-Interface-of-mooKIT-Platform
  <div>
    <img src= "https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" title= "PYTHON" alt= "PYTHON" width="90" height="40"/>&nbsp;
    <img src= "https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white" title= "R" alt= "R" width="90" height="40"/>&nbsp;
    <img src= "https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white" title= "Plotly" alt= "Plotly" width="90" height="40"/>&nbsp;
    <img src= "https://img.shields.io/badge/SciPy-654FF0?style=for-the-badge&logo=SciPy&logoColor=white" title= "SciPy" alt= "SciPy" width="90" height="40"/>&nbsp;
    <img src= "https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white" title= "Pandas" alt= "Pandas" width="90" height="40"/>&nbsp;
    <img src= "https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white" title= "MongoDB" alt= "MongoDB" width="90"     height="40"/>&nbsp;
    <img src= "https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white" title= "MYSQL" alt= "MYSQL" width="90" height="40"/>&nbsp;
   </div>



## INTRODUCTION 🙋‍♂️
  
  * mooKIT is an open source MOOC Management System designed & developed at IIT Kanpur to address the challenges in hosting, Managing, Scaling to the local needs of the     MOOC Courses
  * Intially mooKIT was built upon R,Shiny languages which makes difficult to provide the complex visualizations of the data. I as an intern at IIT Kanpur redesigned the entire Analytical Interface of the mooKIT platform using Plotly Dash.
  * Also, built an ML model to predic the dropout rates from MOOC Courses
  
 ## PROBLEM STATEMENT 🤔
 
 * One of the enhanced feature includes updating multiple graphs/plots when there is a change in single input. Plotly Dash is utilized for this enhancement.
 * One of the requirement is to develop ML model to predict the Dropout rates from MOOC Courses. There are few challenges involved in it. Like the unavailability of the data in proper format, Missing label values for the supervised problem
 
 ## DEVELOPING ML MODELS & RESEARCH WORK 💻
 * The data for this project was in MySQL, MongoDB dumps from which data is extracted & Analyzed.
 * Intially, to explore the different of ways of solving this type of problems. I explored different research papers on Dropout Predictions to understand the general features that were considered and evaluated during this search.
 * The featues that discovered to make an impact are : **Lecture Percentage**, **Quiz Percentage**, **Video Percentage**. The nect challenge is the Unavailability of the labels in the data.
 * From the Certifications Data, people who have been awared certificates were considered as 'not dropouts' and people who did not receive certificates were considered as 'dropouts'. Among the people who were considered as dropouts, outliers like People who have good percentage of all the features but still did not receive certificates were not considered as dropouts. These are the few outlier conditions that are assumed in the project
 * After Extensive Data Cleaning, Data Exploration, Feature Engineering, Feature Selection ML models were trained with different hyper parameters.
 * Comparison of Models was based on different Model metrics and SVM is found to have better performance than other models.
 
