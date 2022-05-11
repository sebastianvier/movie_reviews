import pandas as pd
import numpy as np 

## sklearn
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import recall_score, precision_score, f1_score, accuracy_score

## nltk
from nltk import word_tokenize          
from nltk.stem import WordNetLemmatizer 


## Classes


## Functions

def print_report(y_true, prediction):
    print('Confusion Matrix')
    print(confusion_matrix(y_true, prediction))
    print("\n")
    print('Classification Report')
    print(classification_report(y_true, prediction))
    print("\n")
    print("Other Metrics:")
    print(f'Pression Score: {precision_score(y_true, prediction)}')
    print(f'Accuracy Score: {accuracy_score(y_true, prediction)}')
    print(f'Recall Score: {recall_score(y_true, prediction)}')
    print(f'f1 Score {f1_score(y_true, prediction)}')
    
def check_model(clf, X_test, y_test):
    prediction = clf.predict(X_test)
    print_report(y_test, prediction)
    return prediction


def vectorize_X(vectorizer, X_train, X_test):
    X_train_vectorized = vectorizer.fit_transform(X_train)
    X_test_vectorized  = vectorizer.transform(X_test)
    return X_train_vectorized, X_test_vectorized

