import pandas as pd
import numpy as np

def process_data(data):
    process_sex(data)
    process_name(data)
    process_age(data)
    process_embarked(data)
    process_title(data)
    
    data.drop(['Name', 'Embarked', 'Title'], axis=1, inplace=True)
    #print(data)
    
    return data

def process_sex(df):
    df['Sex'] = df['Sex'].map({'male': 1, 'female':0})

def process_name(df):
    df['Title'] = df.Name.str.extract(' ([A-Za-z]+)\.', expand=False)


def process_age(df):
    df.loc[df['Age'] <= 16, 'Age'] = 0
    df.loc[(df['Age'] > 16) & (df['Age'] <= 32), 'Age'] = 1
    df.loc[(df['Age'] > 32) & (df['Age'] <= 48), 'Age'] = 2
    df.loc[(df['Age'] > 48) & (df['Age'] <= 64), 'Age'] = 3
    df.loc[(df['Age'] > 64), 'Age'] = 4
    
def process_embarked(df):
    embarked = df['Embarked'].values
#    
    df['Embarked_Q'] = 1 if embarked == 'Q'else 0
    df['Embarked_S'] = 1 if embarked == 'S' else 0
    
def process_title(df):
    title = df['Title'].values
    df['Title_Miss'] = 1 if title == 'Miss' else 0
    df['Title_Mr'] = 1 if title == 'Mr' else 0
    df['Title_Mrs'] = 1 if title == 'Mrs' else 0
    df['Title_Rare'] = 1 if title == 'Rare' else 0
    
    
    
    
    
    
    
    
