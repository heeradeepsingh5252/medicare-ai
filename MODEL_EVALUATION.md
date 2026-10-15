# MediCare AI: Model Evaluation Report

## 1. Model Overview

- **Algorithm:** Random Forest Classifier
- **Task:** Binary classification of Negative and Positive outcomes
- **Training/testing split:** 80% training and 20% testing
- **Random state:** 42

## 2. Evaluation Metrics

| Metric | Score |
|---|---:|
| Accuracy | 0.77 |
| Negative class F1-score | 0.75 |
| Positive class Precision | 0.76 |
| Positive class Recall | 0.81 |
| Positive class F1-score | 0.78 |
| Macro-average F1-score | 0.77 |
| Weighted-average F1-score | 0.77 |

## 3. Confusion Matrix

```text
[[21, 8],
 [ 6, 25]]
```

Assuming the class order is Negative followed by Positive:

- True Negatives: 21
- False Positives: 8
- False Negatives: 6
- True Positives: 25

## 4. Interpretation

The model correctly classified 46 of the 60 test records, giving an accuracy of approximately 77%.

The recall for the Positive class was 0.81, meaning the model identified approximately 81% of the actual Positive cases in this test set.

The precision for the Positive class was 0.76, meaning approximately 76% of the records predicted as Positive were actually Positive in this test set.

## 5. Limitations

- Results are based on a single train-test split.
- The test set contains only 60 records.
- Further validation, cross-validation, and checks for data leakage are needed.
- These results do not establish clinical reliability or medical diagnostic accuracy.

**Disclaimer:** MediCare AI is an educational prototype and is not intended to replace professional medical advice, diagnosis, or treatment.

## 6. Cross-Validation

The model was evaluated using 5-fold stratified cross-validation on the training data.

- **Fold accuracy scores:** 0.667, 0.708, 0.729, 0.646, 0.688
- **Mean cross-validation accuracy:** 0.688 (68.8%)
- **Standard deviation:** 0.029
- **Held-out test accuracy:** 0.800 (80.0%)

Cross-validation provides a more robust estimate of model consistency across different training-data folds. Results should be interpreted cautiously because the dataset is small and the model has not been clinically validated.