import streamlit as st
import pandas as pd
import pickle

# Load the impact score pickle file
with open("impactscore_model.pkl", "rb") as file:
    player_impact = pickle.load(file)

# Streamlit UI Elements
st.title("IPL Impact Score Calculator")

# User input for match ID
match_id = st.number_input("Enter Match ID", min_value=0, step=1)

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

st.sidebar.write("Built by Vijay 🔥")
