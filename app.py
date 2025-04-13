import streamlit as st
import pandas as pd
import pickle
import seaborn as sns
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="IPL Impact Score", layout="centered")

# Load the three pickle files
with open("is_player_model_v1.2.pkl", "rb") as file:
    player_impact = pickle.load(file)

with open("is_overwise_model_v1.2.pkl", "rb") as file:
    impact_overwise = pickle.load(file)

with open("is_phasewise_model_v1.2.pkl", "rb") as file:
    impact_phasewise = pickle.load(file)

# Load the impact score pickle file
with open("is_model_v1.1.pkl", "rb") as file:
    player_impact = pickle.load(file)

# Streamlit UI Elements
st.title("IPL Impact Score")

# Match ID input
match_id = st.number_input("Enter Match ID", min_value=0, step=1)
st.info("Open the specific match on ESPNcricinfo and copy the long number at the end of the URL.")

# Impact type selector as tiles
impact_type = st.radio(
    "Select Impact Score Type",
    ["Player-wise", "Over-wise", "Phase-wise"],
    horizontal=True
)

# Proceed if match ID is entered
if match_id:

    if impact_type == "Player-wise":
        df_filtered = player_impact[player_impact["p_match"] == match_id].reset_index(drop=True)
        selected_columns = ["player", "bat_raw", "bat_adj", "ball_raw", "ball_adj", "total"]
        df_filtered = df_filtered[selected_columns]

        if not df_filtered.empty:
            st.write(f"Impact Scores for Match {match_id}")
            st.dataframe(df_filtered)
        else:
            st.warning("No data found for the entered Match ID.")

    elif impact_type == "Over-wise":
        df_filtered = impact_overwise[impact_overwise["p_match"] == match_id]

        if not df_filtered.empty:
            st.subheader("Over-wise Impact Score")
            fig, ax = plt.subplots(figsize=(14, 6))
            sns.barplot(data=df_filtered, x='over', y='impact_bat', hue='team_bat', ax=ax)

            ax.set_title('Over-wise Impact Score')
            ax.set_xlabel('Over')
            ax.set_ylabel('Impact Score')
            ax.set_xticks(range(0, 20))
            ax.set_xticklabels([str(i+1) for i in range(20)])
            ax.legend(title='Team')
            ax.grid(axis='y', linestyle='--', alpha=0.6)
            st.pyplot(fig)
        else:
            st.warning("No data found for the entered Match ID.")

    elif impact_type == "Phase-wise":
        df_filtered = impact_phasewise[impact_phasewise["p_match"] == match_id]

        if not df_filtered.empty:
            st.subheader("Phase-wise Impact Score")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(data=df_filtered, x='phase', y='impact_bat', hue='team_bat', ax=ax)

            ax.set_title('Phase-wise Impact Score')
            ax.set_xlabel('Match Phase')
            ax.set_ylabel('Impact Score')
            ax.grid(axis='y', linestyle='--', alpha=0.6)
            ax.legend(title='Team')
            st.pyplot(fig)
        else:
            st.warning("No phase-wise data found for the entered Match ID.")

# Sidebar footer
st.sidebar.write("Built by [Vijay](https://www.linkedin.com/in/vijay-sundaram/)", unsafe_allow_html=True)
