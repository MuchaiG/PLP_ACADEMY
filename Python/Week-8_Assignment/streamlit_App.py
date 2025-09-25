import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("metadata_cleaned.csv", low_memory=False)
df = load_data()
# Page Config
st.set_page_config(page_title="CORD-19 Research Explorer", layout="wide")

# Title & Description
st.title("CORD-19 Research Analysis Dashboard")
st.markdown("""
Explore COVID-19 research trends using the CORD-19 dataset.  
Use the filters on the sidebar to interact with the data and visualize trends.
""")

# Sidebar Filters
st.sidebar.header("Filters")
year_range = st.sidebar.slider("Select Year Range", 
                               int(df['year'].min()), 
                               int(df['year'].max()), 
                               (2019, 2023))

journal_filter = st.sidebar.multiselect(
    "Filter by Journal", 
    options=sorted(df['journal'].unique()), 
    default=[]
)

# Filter data based on user input
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]
if journal_filter:
    filtered_df = filtered_df[filtered_df['journal'].isin(journal_filter)]

# Show Sample Data
st.subheader("Sample of the Data")
st.dataframe(filtered_df.head(10))

# Visualization 1: Publications Over Time
st.subheader("Number of Publications Over Time")
papers_per_year = filtered_df['year'].value_counts().sort_index()
fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.barplot(x=papers_per_year.index, y=papers_per_year.values, ax=ax1)
ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Papers")
st.pyplot(fig1)

# Visualization 2: Top Journals
st.subheader("Top Publishing Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax2)
ax2.set_xlabel("Number of Papers")
ax2.set_ylabel("Journal")
st.pyplot(fig2)

# Visualization 4: Paper Counts by Source
st.subheader("Paper Counts by Source")
source_counts = filtered_df['source_x'].value_counts().head(10)
fig4, ax4 = plt.subplots(figsize=(10, 5))
sns.barplot(y=source_counts.index, x=source_counts.values, ax=ax4)
ax4.set_xlabel("Number of Papers")
ax4.set_ylabel("Source")
st.pyplot(fig4)

st.markdown("---")
st.caption("Built with Streamlit | CORD-19 COVID-19 Research Dataset")
