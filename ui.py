import streamlit as st
import pandas as pd

# Example data
data = pd.DataFrame({
    'Column1': [1, 2, 3, 4, 5],
    'Column2': [10, 20, 30, 40, 50],
    'Column3': [100, 200, 300, 400, 500]
})

# Title for the app
st.title("EDA Dashboard")

# Create tabs for different sections
tabs = st.tabs(["About the Data", "Findings", "Method", "Results"])

with tabs[0]:
    st.header("About the Data")
    st.write("""
        This dataset contains information about different columns that represent various numerical
        values. Below is a summary of the data.
    """)
    st.write(data.describe())  # Display summary statistics of the dataset

with tabs[1]:
    st.header("Findings")
    st.write("""
        The initial analysis shows that the data has a clear linear relationship between columns. We
        can see trends such as Column2 being directly proportional to Column1. Further analysis is
        required to understand correlations.
    """)
    st.write("Here is a correlation matrix between the columns:")
    st.write(data.corr())  # Display correlation matrix

with tabs[2]:
    st.header("Method")
    st.write("""
        The analysis was performed using various methods including statistical analysis, visualizations,
        and machine learning techniques. Below are the methods used for the analysis.
    """)
    st.write("""
        1. Descriptive Statistics: To summarize the main features of the dataset.
        2. Correlation Analysis: To determine the relationship between variables.
        3. Visualizations: Used to understand the data distributions and trends.
    """)

with tabs[3]:
    st.header("Results")
    st.write("""
        The analysis reveals that Column1 and Column2 are highly correlated. The following models
        and techniques were used to validate this hypothesis:
    """)
    st.write("Here is a simple linear regression result between Column1 and Column2:")
    # Sample plotting with Streamlit
    st.line_chart(data[['Column1', 'Column2']])  # Line chart for visualization
