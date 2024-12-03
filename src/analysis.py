# Problem Statement:
# The project, "Healthcare Facility Analysis," aims to study the distribution and accessibility
# of healthcare facilities in rural areas. This involves analyzing publicly available data
# from a government-provided dataset to identify trends, gaps, and key insights related
# to healthcare infrastructure. The dataset includes information such as facility names,
# types, locations, capacities, and service availability. 
#
# Objectives:
# 1. Assess the spatial distribution of healthcare facilities across rural regions.
# 2. Identify underserved areas and recommend improvements for better healthcare access.
# 3. Perform exploratory data analysis (EDA) to uncover patterns and trends.
# 4. Visualize insights using various data visualization techniques to communicate findings.
#
# Data Source:
# The dataset is sourced from NDAP (https://ndap.niti.gov.in/dataset/7035), which includes multiple files:
# - 7035_KEYS: Contains metadata or keys related to the facility data.
# - 7035_METADATA: Provides detailed metadata about each column in the dataset.
# - 7035_source_data: The main dataset containing raw healthcare facility data.
# - NDAP_REPORT_7035: A summary report of the dataset.
#
# Methodology:
# 1. Merge and preprocess data from all files to create a unified dataset.
# 2. Clean and handle missing or inconsistent data for better analysis.
# 3. Use statistical methods to analyze facility coverage and identify gaps.
# 4. Develop visualizations like heatmaps, bar charts, and


import pandas as pd
import matplotlib.pyplot as plt

# Load the Source Data CSV
source_data_df = pd.read_csv('data/7035_source_data.csv')

# Handle Missing Values
source_data_df.fillna(0, inplace=True)

# Basic Analysis: Sum of healthcare facilities by state
statewise_source = source_data_df.groupby('srcStateName')[
    ['Functional Sub Centres', 'Functional Primary Health Centres', 'Functional Community Health Centres']
].sum()

# Visualization: Facilities by state (Source Data)
plt.figure(figsize=(12, 8))
statewise_source.plot(kind='bar', stacked=True, figsize=(12, 8), color=['#FFA07A', '#20B2AA', '#9370DB'])
plt.title('Healthcare Facilities by State (Source Data)')
plt.xlabel('State')
plt.ylabel('Number of Facilities')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('visuals/source_facilities_by_state.png')  # Save the plot
plt.show()

# Save Aggregated Data
statewise_source.to_csv('output/source_aggregated_data.csv')

# Load the NDAP Report Data CSV
report_df = pd.read_csv('data/NDAP_REPORT_7035.csv')

# Handle Missing Values
report_df.fillna(0, inplace=True)

# Basic Analysis: Sum of healthcare facilities by district
districtwise_report = report_df.groupby('srcDistrictName')[
    ['Functional Sub Centres', 'Functional Primary Health Centres', 'Functional Community Health Centres']
].sum()

# Visualization: Facilities by district (NDAP Report Data)
plt.figure(figsize=(12, 8))
districtwise_report.plot(kind='bar', stacked=True, figsize=(12, 8), color=['#8A2BE2', '#5F9EA0', '#DC143C'])
plt.title('Healthcare Facilities by District (NDAP Report)')
plt.xlabel('District')
plt.ylabel('Number of Facilities')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('visuals/report_facilities_by_district.png')  # Save the plot
plt.show()

# Save Aggregated Data
districtwise_report.to_csv('output/report_aggregated_data.csv')
