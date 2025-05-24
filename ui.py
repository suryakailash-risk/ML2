import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage

# Load data
# @st.cache_data
# def load_data():
#     df = pd.read_csv("Parish_Overall_data.csv")
#     return df

st.title("Unsupervised Learning")
