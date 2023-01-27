# ML-tveets-about-Ukrain-analysis

This paper analyzes data set and aims to create machine learning model that can classify twitter tweets about Ukraine into positive and negative. The purpose of work is educational.

## Data analysis and modeling
notebooks/modelling.ipynb
### Main content:
#### Importing Dependencies
#### Importing dataset and First look
##### Data cleaning
##### Drop unused columns
##### Remove dublicates
##### Remove non-english posts
##### Save cleaned date to .csv
##### Plotting word clouds
##### Conclusions about data set
#### Preprocess Text and Count Vectorizer
##### Lower Casing
##### Replacing URLs
##### Removing Usernames
##### Replacing Emojis
##### Removing stopwords
##### Lemmatizing and Stemmerizing
#### Write Text Transformer
##### How transformer works
#### Pipeline
#### Spliting date to train and test
#### Training models
#### Metrics
#### Try to balance size of train and test
##### Spliting date to train and test
##### Training models
##### Metrics
#### Tune of hyperparams
##### LogisticRegression
##### DecisionTreeClassifier
##### RandomForestClassifier
##### XGBClassifier
#### Conclusions about classification
#### Exporting best model

