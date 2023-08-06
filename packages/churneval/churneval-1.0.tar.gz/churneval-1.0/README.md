# Package "churneval"

#### **Version:** 1.0

#### **Author:** *Soumi De*

#### **Maintained by:** Soumi De <<soumi.de@res.christuniversity.in>>

#### **Description:** 
churneval is a package to evaluate models used in churn classification. The evaluation metrics include accuracy, sensitivity, specificity, precision, F1-score and top-decile lift.

#### **License:** GPL-3

#### **Date:** 12th November, 2021
<br>

___


### **Function:**
    get_performance_metrics               Function that returns evaluation metrics

___
<br>

### **Usage:**

from churneval import get_performance_metrics

get_performance_metrics(model_name, true_class, predicted_class, predicted_probs)

### **Arguments:**
* model_name: 		Abbreviated name of the churn model (in text)
* true_class: 		A dataframe of true class labels with shape (n,1)
* predicted_class: 	An array of binary predicted class with shape (n,)
* predicted_probs:	An array of predicted class probabilities with shape (n,)

### **Returned Values:**

A dataframe consisting of elements given below:
* Model_Name: Abbreviated name of the churn model
* Accuracy:		Accuracy of churn model
* Confusion Matrix:	A 2X2 array representing confusion matrix
* Precision:		Precision value
* Sensitivity:		Sensitivity value
* Specificity:		Specificity value
* F1-score:		F1-score
* ROC_score:		Area under the curve
* top_dec_lift:		Top decile lift value
