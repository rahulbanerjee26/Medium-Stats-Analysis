import pandas as pd
import matplotlib.pyplot as plt 
import streamlit as st
import seaborn as sns 
plt.style.use("dark_background")
st.set_page_config(layout = "wide")

def plot_top_5(df, colName):
    top5 = df.sort_values(by=[colName],ascending = False)[:5]
    fig,ax = plt.subplots(figsize = (15,15))
    ax = sns.barplot(x = colName, y = "title", data = top5)
    return fig

def categorizeArticle(readTime):
    if 1<= readTime <=3:
        return '1-3 mins'
    elif 4 <= readTime <= 6:
        return '4-6 mins'
    elif 7<= readTime <= 9:
        return '7-9 mins'
    else:
        return '9+ mins'


st.title("Medium Stats")

df = pd.read_json("story.json")
st.dataframe(df)

st.title("Summary")

minReadSum = df['minRead'].sum()
minReadSumString = f'{minReadSum} minutes' if minReadSum < 60 else f'{int(minReadSum/60)} hours and {minReadSum%60} minutes'
totalNumViews = df['views'].sum()
totalNumReads = df['reads'].sum()
totalNumFans = df['numFans'].sum()
numArticles = len(df)

st.subheader(f'You have written a total of {numArticles} articles')

st.subheader(f'Your articles have a total read time of {minReadSumString}. In total, they have been viewed {totalNumViews} times and read {totalNumReads} times. Your articles have received {totalNumFans} upvotes')

st.subheader(f'On average, your article has a read time of {round(minReadSum/numArticles , 2)} minutes. They get {int(totalNumViews/numArticles) } views, {int(totalNumReads/numArticles)} reads and {int(totalNumFans/numArticles)} fans')

st.title("Your Top 5")

colNames = ["views" , "reads" , "numFans" , "readPercentage"]
p1,p2 = st.beta_columns(2)
for idx,colName in enumerate(colNames):
    curr = p1 if idx%2==0 else p2
    curr.subheader(f'Top 5 by {colName}')
    curr.pyplot(plot_top_5(df, colName))


p1.title("Publications Distribution")

df['publication'] = df.apply( lambda row : row['publication'] if row['publication'] != 'View story' else "No Publication" , axis = 1)

Publicationscount = df['publication'].value_counts()
fig = plt.figure(figsize=(20,20))
plt.pie(Publicationscount, labels = Publicationscount.index,autopct='%1.0f%%')
p1.pyplot(fig)

df['articleCategory'] = df.apply(lambda row: categorizeArticle(row['minRead']) , axis =1)
p2.title("Article Read Time")
fig,ax = plt.subplots(figsize=(25,25))
ax = sns.countplot(data=df,x='articleCategory',order=['1-3 mins','4-6 mins','7-9 mins','9+ mins'])
p2.pyplot(fig)
