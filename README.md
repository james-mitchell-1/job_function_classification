# job_function_classification

## Overview
An investigation into the viability of classifying a job's function from the job 'role' or 'title' using a  TFIDF model.

- Exploratory Data Anaylis
    - 'notebooks/job_function_exploration.ipynb'

- Cleaning
    - 'scripts/clean_aff_data.py'

- Modeling and Classification
    - 'notebooks/'job_function_classification.ipynb'

## Dataset
The data comes from a non-profit organization in the education sector.  As we'll see, the data gathered by the organization has evolved over time resulting in inconsitant classes and field use cases.  Each of the 109,485 records represent a single job and has been limited to the following variables:

| Column | Missing Values | Data Type |
|---|---|---|
| affiliate_id_18 | 109485 | int64 |
| function  | 90572 | str |
| title  | 51280 | str |
| role  | 46778 | str |
| management_level  | 70720 | str |
| role_level  | 29230 | float64 |

A sample of the raw data, as well as the cleaned data, can be found in the data folder.

## Tools Used
Python, pandas, matplotlib, seaborn, nltk, and sklearn

## Key Findings and Recomendations
- Job 'Role' and 'Title' have been used interchangably (though rarely simultaneously) over time.

- Job 'Function', 'Role Level', and 'Management Level' contain redundant variations of the same classes.  Distinct classes may have overlap with other classes.
    - This will impact the performance of our classificatio model (as evident in the high levels of misclassification for 'General Managment', and 'Program and Product Management', for example)

    - Increasing the distinctness of classes through consolidation may improve performance.

- Job 'Function' classification using a TFIDF model is highly dependent on class.
    - The model does reasonably well classifying 'Academics (Teaching & Learning)', 'Data / Analytics / Research', and 'General Management'

    - The model struggles to perform well on all other classes

- Deployment of the model will require class specific tuning around on acceptable error, similarity between classes, and the impact of misclassification on organizational decision making. 
