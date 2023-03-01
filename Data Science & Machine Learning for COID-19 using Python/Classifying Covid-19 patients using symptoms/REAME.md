# Classifying Covid-19 patients using symptoms

# Problem - Chest X-Ray Classification

# Problem Statement
- To classify a given chest x-ray into one of the following classes:
    - Covid-19 (219)
    - Pneumonia (1345)
    - Normal (1341)
- Total data availble for covid-9 x-rays: 219
- Class imbalance

# Class Imbalance
- Imbalanced classification refers to a classification predictive modeling problem where the number of examples n the training dataset for each class label is not balanced.
- That is where the class distribution is not equal or clos to equal, and is instead biased or skewed.
- This imbalance can be slight or strong. Depending on the sample size, ratios from 1:2 to 1:10 can be understood as a slight imbalance and ratios greater than 1:10 can be understood as a strong imbalance.
- In both cases, the data with the class imbalance problem must be treated with special techniques.
- Our data is slightly imbalanced with two classes having same data. And one class having less data.

# The metric trap
- One of the major issues that novice users fall into when dealing with unbalanced datasets relates to the metrics used to evaluate their model. Using simples metrics like accuracy_score can be misleading.
- In a dataset with highly unbalanced classes, if the classifier always "predicts" the most common class without performing any analysis of the features, it will still have a high accuracy rate, obviously illusory.
- Coming to our dataset, metric trap shouldn't be a big problem since we have two classes with almost equal examples so its not viable for the classifier to perform classification without any analysis on the features and just classify one class. It wouldn't lead t higher accuracy.