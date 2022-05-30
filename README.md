# NLP Project Based on IMBD

## __Sentiment analysis model trained in this beloved database__



### Objective for the Project
1)  Train two models on IMBD Database  &nbsp; :white_check_mark:
2)  Store both models as sav files &nbsp;  :white_check_mark:
3) Test the models predictability on a different source (i.e. Amazon Reviews) &nbsp; :white_check_mark:
4) Deploy the best model using Streamlit 

### Data
The data for this project was obtained through two kaggle repositories:
#### IMDB
https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

#### Amazon Reviews
https://www.kaggle.com/datasets/bittlingmayer/amazonreviews

### Files

This repository contains 3 folders.  2 are the test made for finding good parameters for the model. The other has the models being tested against amazon and even twitter.  Be ware some of the models take some time to run. <br>

The repository also contains a function.py for reusable functions.

### Results
Two types of model where tested: 1)  Multinomial Naive Bayes and a 2) Suppor Vector Classifier. Both Models perform a little bit above 80% on the amazon reviews database. A pseudo Cross-Validation was performed to check wether Variance of the model in this situation. The decisions was to run the model in different sections of the amazon reviews comments and then look at the mean and the standard deviation. 

<br> Even though both models performed similar, the SVC was selected for the classifier because it provided useful information on the probability of the result specially on the false positives and false negatives.

### Resources
https://www.kaggle.com/<br>
https://www.kaggle.com/code/trunganhdinh/spam-classification<br>
https://machinelearningmastery.com/<br>
https://www.youtube.com/c/joshstarmer