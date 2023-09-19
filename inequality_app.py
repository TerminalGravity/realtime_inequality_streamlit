import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_excel("Full Database.xlsx")

data = load_data()

# App title
st.title("Realtime Inequality Insights")

# Data overview
if st.checkbox("Show raw data"):
    st.subheader("Data Overview")
    st.write(data)

# Define a color map based on groups
color_map = {
    "Total": "#FFFFFF",
    "Bottom 50%": "#74AF14",
    "Middle 40%": "#16ABFE",
    "Top 10%": "#EE1717",
    "Top 1%": "#DB9D00",
    "Top 0.1%": "#8021E0",
    "Top 0.01%": "#EB34E5"
}

# Income and Wealth Growth Over Time
st.subheader("Income and Wealth Growth Over Time")
selected_group1 = st.selectbox("Select Group for Growth Analysis", data['group'].unique())
filtered_data1 = data[data['group'] == selected_group1]

# Plotting post-tax income per unit
fig_income = px.line(filtered_data1, x='year', y='posttax_income_per_unit', color='group',
                     color_discrete_map=color_map, 
                     title=f"Post-tax Income Per Unit Over Time for {selected_group1}")
st.plotly_chart(fig_income)

# Plotting wealth per unit
fig_wealth = px.line(filtered_data1, x='year', y='wealth_per_unit', color='group',
                     color_discrete_map=color_map, 
                     title=f"Wealth Per Unit Over Time for {selected_group1}")
st.plotly_chart(fig_wealth)

# ... (similar changes for the other charts)


# Share of Wealth and Income
st.subheader("Share of Wealth and Income")
selected_group2 = st.selectbox("Select Group for Share Analysis", data['group'].unique(), key='group2')
filtered_data2 = data[data['group'] == selected_group2]

# Bar chart for post-tax income share
fig_income_share = px.bar(filtered_data2, x='year', y='posttax_income_share',
                          color_discrete_map=color_map, 
                          title=f"Post-tax Income Share for {selected_group2}")
st.plotly_chart(fig_income_share)

# Bar chart for wealth share
fig_wealth_share = px.bar(filtered_data2, x='year', y='wealth_share',
                          color_discrete_map=color_map, 
                          title=f"Wealth Share for {selected_group2}")
st.plotly_chart(fig_wealth_share)

# Population vs. Wealth/Income Share Scatter Plots
st.subheader("Population vs. Wealth/Income Share")
selected_group3 = st.selectbox("Select Group for Population vs. Share Analysis", data['group'].unique(), key='group3')
filtered_data3 = data[data['group'] == selected_group3]

# Scatter plot for population vs post-tax income share
fig_pop_income = px.scatter(filtered_data3, x='population', y='posttax_income_share',
                            color_discrete_map=color_map, 
                            title=f"Population vs. Post-tax Income Share for {selected_group3}")
st.plotly_chart(fig_pop_income)

# Scatter plot for population vs wealth share
fig_pop_wealth = px.scatter(filtered_data3, x='population', y='wealth_share',
                            color_discrete_map=color_map, 
                            title=f"Population vs. Wealth Share for {selected_group3}")
st.plotly_chart(fig_pop_wealth)
