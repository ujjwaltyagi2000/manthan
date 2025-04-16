import streamlit as st
import pandas as pd
import numpy as np

# import matplotlib.pyplot as plt
# import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page configuration
st.set_page_config(
    page_title="Manthan - Lok Sabha Elections Analysis",
    page_icon="🗳️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Function to load data
@st.cache_data
def load_data():
    # Update these paths to where your data files are stored
    df_ls_2019 = pd.read_csv("data/dashboard/candidate_background_2019.csv")
    df_ls_2024 = pd.read_csv("data/dashboard/candidate_background_2024.csv")
    return df_ls_2019, df_ls_2024


# Load the data
try:
    df_ls_2019, df_ls_2024 = load_data()
    data_loaded = True
except Exception as e:
    st.error(f"Error loading data: {e}")
    data_loaded = False

# App title and introduction
st.title("🗳️ Manthan - Lok Sabha Elections Analysis")
st.markdown(
    """
This app provides insights into the Indian Lok Sabha Elections for 2019 and 2024, 
analyzing candidate profiles, party performance, and demographic trends.
"""
)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select a page:",
    [
        "Home",
        "Candidate Demographics",
        "criminal_cases",
        "Education & Assets",
        "Party Analysis",
    ],
)

# Home page
if page == "Home":
    st.header("Overview of Lok Sabha Elections 2019 vs 2024")

    if data_loaded:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("2019 Election Statistics")
            st.metric("Total Candidates", f"{len(df_ls_2019):,}")
            st.metric("Political Parties", f"{df_ls_2019['party'].nunique():,}")

        with col2:
            st.subheader("2024 Election Statistics")
            st.metric("Total Candidates", f"{len(df_ls_2024):,}")
            st.metric("Political Parties", f"{df_ls_2024['party'].nunique():,}")

        # Key insights section
        st.header("Key Insights")
        st.markdown(
            """
        - **Candidate Demographics**: Analysis of age, gender, and other demographic factors
        - **Criminal Background**: Trends in criminal cases against candidates
        - **Education & Assets**: Educational qualifications and financial assets of candidates
        - **Party Analysis**: Performance and candidate selection by political parties
        
        Navigate through the sidebar to explore detailed insights on each topic.
        """
        )

        # Show a sample of the data
        st.subheader("Sample Data from 2024 Elections")
        st.dataframe(df_ls_2024.head())

    else:
        st.warning("Please upload the data files to continue.")

# Candidate Demographics page
elif page == "Candidate Demographics":
    st.header("Candidate Demographics")

    if data_loaded:
        # Age distribution tab
        st.subheader("Age Distribution")

        tab1, tab2 = st.tabs(["2019", "2024"])

        with tab1:
            fig = px.histogram(
                df_ls_2019,
                x="Age",
                title="Age Distribution of Candidates (2019)",
                labels={"Age": "Age", "count": "Number of Candidates"},
                nbins=50,
                color_discrete_sequence=["#1f77b4"],
            )
            st.plotly_chart(fig, use_container_width=True)

            # Age statistics
            col1, col2, col3 = st.columns(3)
            col1.metric("Average Age", f"{df_ls_2019['Age'].mean():.1f}")
            col2.metric("Minimum Age", f"{df_ls_2019['Age'].min()}")
            col3.metric("Maximum Age", f"{df_ls_2019['Age'].max()}")

        with tab2:
            fig = px.histogram(
                df_ls_2024,
                x="Age",
                title="Age Distribution of Candidates (2024)",
                labels={"Age": "Age", "count": "Number of Candidates"},
                nbins=50,
                color_discrete_sequence=["#ff7f0e"],
            )
            st.plotly_chart(fig, use_container_width=True)

            # Age statistics
            col1, col2, col3 = st.columns(3)
            col1.metric("Average Age", f"{df_ls_2024['Age'].mean():.1f}")
            col2.metric("Minimum Age", f"{df_ls_2024['Age'].min()}")
            col3.metric("Maximum Age", f"{df_ls_2024['Age'].max()}")

        # Gender distribution
        st.subheader("Gender Distribution")

        col1, col2 = st.columns(2)

        with col1:
            # Calculate gender distribution for 2019
            gender_2019 = df_ls_2019["Gender"].value_counts().reset_index()
            gender_2019.columns = ["Gender", "Count"]

            fig = px.pie(
                gender_2019,
                names="Gender",
                values="Count",
                title="Gender Distribution (2019)",
                color_discrete_sequence=px.colors.qualitative.Pastel,
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Calculate gender distribution for 2024
            gender_2024 = df_ls_2024["Gender"].value_counts().reset_index()
            gender_2024.columns = ["Gender", "Count"]

            fig = px.pie(
                gender_2024,
                names="Gender",
                values="Count",
                title="Gender Distribution (2024)",
                color_discrete_sequence=px.colors.qualitative.Pastel,
            )
            st.plotly_chart(fig, use_container_width=True)

        # Comparison of gender representation
        st.subheader("Gender Representation Comparison (2019 vs 2024)")

        # Create comparison dataframe
        gender_2019_pct = (
            df_ls_2019["Gender"].value_counts(normalize=True).reset_index()
        )
        gender_2019_pct.columns = ["Gender", "Percentage"]
        gender_2019_pct["Year"] = "2019"

        gender_2024_pct = (
            df_ls_2024["Gender"].value_counts(normalize=True).reset_index()
        )
        gender_2024_pct.columns = ["Gender", "Percentage"]
        gender_2024_pct["Year"] = "2024"

        gender_comparison = pd.concat([gender_2019_pct, gender_2024_pct])
        gender_comparison["Percentage"] = gender_comparison["Percentage"] * 100

        fig = px.bar(
            gender_comparison,
            x="Gender",
            y="Percentage",
            color="Year",
            barmode="group",
            title="Gender Distribution Comparison (2019 vs 2024)",
            labels={"Percentage": "Percentage (%)", "Gender": "Gender"},
        )
        st.plotly_chart(fig, use_container_width=True)

    else:
        st.warning("Please upload the data files to continue.")

# Criminal Cases page
elif page == "criminal_cases":
    st.header("Criminal Cases Analysis")

    if data_loaded:
        st.subheader("Distribution of Criminal Cases")

        # Create tabs for different years
        tab1, tab2 = st.tabs(["2019", "2024"])

        with tab1:
            # Distribution of criminal cases in 2019
            criminal_2019 = df_ls_2019["criminal_cases"].value_counts().reset_index()
            criminal_2019.columns = ["Number of Cases", "Count"]

            fig = px.bar(
                criminal_2019.head(20),
                x="Number of Cases",
                y="Count",
                title="Distribution of Criminal Cases (2019)",
                labels={
                    "Number of Cases": "Number of Criminal Cases",
                    "Count": "Number of Candidates",
                },
            )
            st.plotly_chart(fig, use_container_width=True)

            # Percentage of candidates with criminal cases
            criminal_pct_2019 = (df_ls_2019["criminal_cases"] > 0).mean() * 100
            st.metric("Candidates with Criminal Cases (%)", f"{criminal_pct_2019:.1f}%")

        with tab2:
            # Distribution of criminal cases in 2024
            criminal_2024 = df_ls_2024["criminal_cases"].value_counts().reset_index()
            criminal_2024.columns = ["Number of Cases", "Count"]

            fig = px.bar(
                criminal_2024.head(20),
                x="Number of Cases",
                y="Count",
                title="Distribution of Criminal Cases (2024)",
                labels={
                    "Number of Cases": "Number of Criminal Cases",
                    "Count": "Number of Candidates",
                },
            )
            st.plotly_chart(fig, use_container_width=True)

            # Percentage of candidates with criminal cases
            criminal_pct_2024 = (df_ls_2024["criminal_cases"] > 0).mean() * 100
            st.metric("Candidates with Criminal Cases (%)", f"{criminal_pct_2024:.1f}%")

        # Analysis by top parties
        st.subheader("Criminal Cases by Major Political Parties")

        # Get top 10 parties by candidate count
        top_parties_2019 = df_ls_2019["party"].value_counts().head(10).index.tolist()
        top_parties_2024 = df_ls_2024["party"].value_counts().head(10).index.tolist()
        top_parties = list(set(top_parties_2019 + top_parties_2024))

        # Create comparison dataframe for 2019
        party_criminal_2019 = (
            df_ls_2019[df_ls_2019["party"].isin(top_parties)]
            .groupby("party")["criminal_cases"]
            .mean()
            .reset_index()
        )
        party_criminal_2019["Year"] = "2019"

        # Create comparison dataframe for 2024
        party_criminal_2024 = (
            df_ls_2024[df_ls_2024["party"].isin(top_parties)]
            .groupby("party")["criminal_cases"]
            .mean()
            .reset_index()
        )
        party_criminal_2024["Year"] = "2024"

        # Combine data
        party_criminal_comparison = pd.concat(
            [party_criminal_2019, party_criminal_2024]
        )

        fig = px.bar(
            party_criminal_comparison,
            x="party",
            y="criminal_cases",
            color="Year",
            barmode="group",
            title="Average Criminal Cases by Party (2019 vs 2024)",
            labels={
                "criminal_cases": "Average Number of Criminal Cases",
                "party": "Political Party",
            },
        )
        st.plotly_chart(fig, use_container_width=True)

    else:
        st.warning("Please upload the data files to continue.")

# Education & Assets page
elif page == "Education & Assets":
    st.header("Education & Financial Analysis")

    if data_loaded:
        # Education Analysis
        st.subheader("Educational Qualifications")

        tab1, tab2 = st.tabs(["2019", "2024"])

        with tab1:
            # Education distribution for 2019
            education_2019 = df_ls_2019["education"].value_counts().reset_index()
            education_2019.columns = ["education", "Count"]
            education_2019 = education_2019.sort_values("Count", ascending=True)

            fig = px.bar(
                education_2019,
                y="education",
                x="Count",
                title="Educational Qualifications Distribution (2019)",
                orientation="h",
                labels={
                    "education": "Educational Qualification",
                    "Count": "Number of Candidates",
                },
            )
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            # Education distribution for 2024
            education_2024 = df_ls_2024["education"].value_counts().reset_index()
            education_2024.columns = ["education", "Count"]
            education_2024 = education_2024.sort_values("Count", ascending=True)

            fig = px.bar(
                education_2024,
                y="education",
                x="Count",
                title="Educational Qualifications Distribution (2024)",
                orientation="h",
                labels={
                    "education": "Educational Qualification",
                    "Count": "Number of Candidates",
                },
            )
            st.plotly_chart(fig, use_container_width=True)

        # Assets Analysis
        st.subheader("Assets Distribution")

        # Create toggle for log scale
        use_log_scale = st.checkbox("Use Logarithmic Scale for Assets")

        tab1, tab2 = st.tabs(["2019", "2024"])

        with tab1:
            # Assets distribution for 2019
            fig = px.histogram(
                df_ls_2019,
                x="Total Assets",
                title="Assets Distribution (2019)",
                nbins=50,
                log_x=use_log_scale,
                labels={
                    "Total Assets": "Total Assets (₹)",
                    "count": "Number of Candidates",
                },
            )
            st.plotly_chart(fig, use_container_width=True)

            # Asset statistics
            col1, col2, col3 = st.columns(3)
            col1.metric("Average Assets", f"₹{df_ls_2019['Total Assets'].mean():,.2f}")
            col2.metric("Median Assets", f"₹{df_ls_2019['Total Assets'].median():,.2f}")
            col3.metric("Maximum Assets", f"₹{df_ls_2019['Total Assets'].max():,.2f}")

        with tab2:
            # Assets distribution for 2024
            fig = px.histogram(
                df_ls_2024,
                x="Total Assets",
                title="Assets Distribution (2024)",
                nbins=50,
                log_x=use_log_scale,
                labels={
                    "Total Assets": "Total Assets (₹)",
                    "count": "Number of Candidates",
                },
            )
            st.plotly_chart(fig, use_container_width=True)

            # Asset statistics
            col1, col2, col3 = st.columns(3)
            col1.metric("Average Assets", f"₹{df_ls_2024['Total Assets'].mean():,.2f}")
            col2.metric("Median Assets", f"₹{df_ls_2024['Total Assets'].median():,.2f}")
            col3.metric("Maximum Assets", f"₹{df_ls_2024['Total Assets'].max():,.2f}")

        # Relationship between education and assets
        st.subheader("Relationship: Education & Assets")

        year = st.radio("Select Year:", ["2019", "2024"])

        if year == "2019":
            df = df_ls_2019
        else:
            df = df_ls_2024

        # Group by education and calculate average assets
        edu_assets = df.groupby("education")["Total Assets"].mean().reset_index()
        edu_assets = edu_assets.sort_values("Total Assets")

        fig = px.bar(
            edu_assets,
            y="education",
            x="Total Assets",
            title=f"Average Assets by Educational Qualification ({year})",
            orientation="h",
            labels={
                "education": "Educational Qualification",
                "Total Assets": "Average Total Assets (₹)",
            },
        )
        st.plotly_chart(fig, use_container_width=True)

    else:
        st.warning("Please upload the data files to continue.")

# Party Analysis page
elif page == "Party Analysis":
    st.header("Political Party Analysis")

    if data_loaded:
        # Top parties by number of candidates
        st.subheader("Top Parties by Number of Candidates")

        col1, col2 = st.columns(2)

        with col1:
            # Top parties in 2019
            top_parties_2019 = df_ls_2019["party"].value_counts().head(10).reset_index()
            top_parties_2019.columns = ["party", "Number of Candidates"]

            fig = px.bar(
                top_parties_2019,
                y="party",
                x="Number of Candidates",
                title="Top 10 Parties by Candidates (2019)",
                orientation="h",
                labels={
                    "party": "Political Party",
                    "Number of Candidates": "Number of Candidates",
                },
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Top parties in 2024
            top_parties_2024 = df_ls_2024["party"].value_counts().head(10).reset_index()
            top_parties_2024.columns = ["party", "Number of Candidates"]

            fig = px.bar(
                top_parties_2024,
                y="party",
                x="Number of Candidates",
                title="Top 10 Parties by Candidates (2024)",
                orientation="h",
                labels={
                    "party": "Political Party",
                    "Number of Candidates": "Number of Candidates",
                },
            )
            st.plotly_chart(fig, use_container_width=True)

        # Party characteristics
        st.subheader("Party Characteristics Analysis")

        # Select analysis type
        analysis_type = st.selectbox(
            "Select Analysis Type:",
            ["Average Age", "Gender Diversity", "criminal_cases", "Average Assets"],
        )

        # Get top 10 parties overall
        top_parties_overall = pd.concat(
            [
                df_ls_2019["party"].value_counts().head(10).reset_index(),
                df_ls_2024["party"].value_counts().head(10).reset_index(),
            ]
        )
        top_parties_overall = top_parties_overall.iloc[:, 0].unique().tolist()

        # Filter for selected parties
        selected_parties = st.multiselect(
            "Select Parties to Compare:",
            options=top_parties_overall,
            default=top_parties_overall[:5],
        )

        if selected_parties:
            if analysis_type == "Average Age":
                # Average age by party
                party_age_2019 = (
                    df_ls_2019[df_ls_2019["party"].isin(selected_parties)]
                    .groupby("party")["Age"]
                    .mean()
                    .reset_index()
                )
                party_age_2019["Year"] = "2019"

                party_age_2024 = (
                    df_ls_2024[df_ls_2024["party"].isin(selected_parties)]
                    .groupby("party")["Age"]
                    .mean()
                    .reset_index()
                )
                party_age_2024["Year"] = "2024"

                party_age_comparison = pd.concat([party_age_2019, party_age_2024])

                fig = px.bar(
                    party_age_comparison,
                    x="party",
                    y="Age",
                    color="Year",
                    barmode="group",
                    title="Average Age by Party (2019 vs 2024)",
                    labels={"Age": "Average Age", "party": "Political Party"},
                )
                st.plotly_chart(fig, use_container_width=True)

            elif analysis_type == "Gender Diversity":
                # Calculate female percentage by party
                party_gender_2019 = (
                    df_ls_2019[df_ls_2019["party"].isin(selected_parties)]
                    .groupby("party")["Gender"]
                    .apply(lambda x: (x == "F").mean() * 100)
                    .reset_index()
                )
                party_gender_2019.columns = ["party", "Female Percentage"]
                party_gender_2019["Year"] = "2019"

                party_gender_2024 = (
                    df_ls_2024[df_ls_2024["party"].isin(selected_parties)]
                    .groupby("party")["Gender"]
                    .apply(lambda x: (x == "F").mean() * 100)
                    .reset_index()
                )
                party_gender_2024.columns = ["party", "Female Percentage"]
                party_gender_2024["Year"] = "2024"

                party_gender_comparison = pd.concat(
                    [party_gender_2019, party_gender_2024]
                )

                fig = px.bar(
                    party_gender_comparison,
                    x="party",
                    y="Female Percentage",
                    color="Year",
                    barmode="group",
                    title="Female Candidate Percentage by Party (2019 vs 2024)",
                    labels={
                        "Female Percentage": "Female Candidates (%)",
                        "party": "Political Party",
                    },
                )
                st.plotly_chart(fig, use_container_width=True)

            elif analysis_type == "criminal_cases":
                # Average criminal cases by party
                party_criminal_2019 = (
                    df_ls_2019[df_ls_2019["party"].isin(selected_parties)]
                    .groupby("party")["criminal_cases"]
                    .mean()
                    .reset_index()
                )
                party_criminal_2019["Year"] = "2019"

                party_criminal_2024 = (
                    df_ls_2024[df_ls_2024["party"].isin(selected_parties)]
                    .groupby("party")["criminal_cases"]
                    .mean()
                    .reset_index()
                )
                party_criminal_2024["Year"] = "2024"

                party_criminal_comparison = pd.concat(
                    [party_criminal_2019, party_criminal_2024]
                )

                fig = px.bar(
                    party_criminal_comparison,
                    x="party",
                    y="criminal_cases",
                    color="Year",
                    barmode="group",
                    title="Average Criminal Cases by Party (2019 vs 2024)",
                    labels={
                        "criminal_cases": "Average Number of Criminal Cases",
                        "party": "Political Party",
                    },
                )
                st.plotly_chart(fig, use_container_width=True)

            elif analysis_type == "Average Assets":
                # Average assets by party
                party_assets_2019 = (
                    df_ls_2019[df_ls_2019["party"].isin(selected_parties)]
                    .groupby("party")["Total Assets"]
                    .mean()
                    .reset_index()
                )
                party_assets_2019["Year"] = "2019"

                party_assets_2024 = (
                    df_ls_2024[df_ls_2024["party"].isin(selected_parties)]
                    .groupby("party")["Total Assets"]
                    .mean()
                    .reset_index()
                )
                party_assets_2024["Year"] = "2024"

                party_assets_comparison = pd.concat(
                    [party_assets_2019, party_assets_2024]
                )

                fig = px.bar(
                    party_assets_comparison,
                    x="party",
                    y="Total Assets",
                    color="Year",
                    barmode="group",
                    title="Average Assets by Party (2019 vs 2024)",
                    labels={
                        "Total Assets": "Average Total Assets (₹)",
                        "party": "Political Party",
                    },
                )
                st.plotly_chart(fig, use_container_width=True)

    else:
        st.warning("Please upload the data files to continue.")

# Footer
st.markdown("---")
st.markdown("**Manthan** - Analyzing Indian Lok Sabha Elections 2019 & 2024")
st.markdown("Data source: GitHub repository by ujjwaltyagi2000")
