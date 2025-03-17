import streamlit as st
import pandas as pd
import pickle

# Load the impact score pickle file
with open("impactscore_model_v1.pkl", "rb") as file:
    player_impact = pickle.load(file)

# Streamlit UI Elements
st.title("IPL Impact Score Calculator")

# User input for match ID
match_id = st.number_input("Enter Cricinfo Match ID")

# Info about Match ID
st.info("Open the specific match on ESPNcricinfo and copy the long number at the end of the URL.")

# Check if a valid match ID is entered
if match_id:
    # Filter the player impact table for the selected match
    df_filtered = player_impact[player_impact["p_match"] == match_id][['player', 'impact_bat', 'impact_ball', 'total_impact']].reset_index(drop=True)

    # Display results
    if not df_filtered.empty:
        st.write(f"Impact Scores for Match {match_id}")
        st.dataframe(df_filtered)
    else:
        st.warning("No data found for the entered Match ID.")

st.sidebar.write("Built by [Vijay](https://www.linkedin.com/in/vijay-sundaram/)", unsafe_allow_html=True)











