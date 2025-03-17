import streamlit as st
import pandas as pd
import pickle

# Load the impact score pickle file
with open("impactscore_model_v1.pkl", "rb") as file:
    player_impact = pickle.load(file)

# Info about Match ID
st.info("Enter the Match ID as per the IPL dataset. If you're unsure about the Match ID, refer to the dataset or match details.")

# Streamlit UI Elements
st.title("IPL Impact Score Calculator")

# User input for match ID
match_id = st.text_input("Match ID", placeholder="Enter Match ID")

# Selection for impact type
impact_type = st.radio(
    "Select Impact Type",
    ("Batting Impact", "Bowling Impact", "Total Impact"),
)

# Map selection to column names
impact_column_map = {
    "Batting Impact": "impact_bat",
    "Bowling Impact": "impact_ball",
    "Total Impact": "total_impact",
}
selected_column = impact_column_map[impact_type]

# Check if a valid match ID is entered
if match_id:
    # Filter the player impact table for the selected match
    df_filtered = player_impact[player_impact["p_match"] == match_id][["player", selected_column]].reset_index(drop=True)

    # Display results
    if not df_filtered.empty:
        st.write(f"{impact_type} for Match {match_id}")
        st.dataframe(df_filtered)
    else:
        st.warning("No data found for the entered Match ID.")

# Sidebar with LinkedIn profile
st.sidebar.write("Built by [Vijay 🔥](https://www.linkedin.com/in/vijay)", unsafe_allow_html=True)














