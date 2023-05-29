import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.figure_factory as P

# if we want access local folder in deployment

# data_path = "data\"
# pd.read_csv(data_path+"iris.csv")

# We want to display our data in web application
# st.dataframe()

# st.write() will only show limited number of columns

iris = sns.load_dataset('iris')

st.title('IRIS Dashboard')
st.dataframe(iris)

# For plotting we need to use streamlit syntax
# st.pyplot()

# fig, ax = plt.subplots()
# ax.hist(iris['sepal_length'])

# st.pyplot(fig)

# if we want to create a drop box to select input from user and plot particular histogram
# We want to see Boxplot beside histogram
# We need to use subplots


col_name = st.selectbox(
    'Select your column name',
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width'))

fig, ax = plt.subplots(2)
ax[0].hist(iris[col_name])
ax[1].boxplot(iris[col_name])

st.pyplot(fig)


# Plotly is created on top of seaborn, this is an advanced visualization and simillar to tableau and power BI
# we need to install plotly first


# We can use Plotly charts
# st.plotly_chart()
# streamlit will show the dynamic visualization correctly. Github does not show dynamic visualization


# plotly coding we can do later



