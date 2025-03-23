import streamlit as st
import pandas as pd
import pickle

# Load the impact score pickle file
with open("is_model_v1.1.pkl", "rb") as file:
    player_impact = pickle.load(file)

# Streamlit UI Elements
st.title("IPL Impact Score Calculator")

# User input for match ID
match_id = st.number_input("Enter Match ID", min_value=0, step=1)

# Info about Match ID
st.info("Open the specific match on ESPNcricinfo and copy the long number at the end of the URL.")


# Check if a valid match ID is entered
if match_id:
    # Filter the player impact table for the selected match
    df_filtered = player_impact[player_impact["p_match"] == match_id].reset_index(drop=True)

    # Select only the required columns
    selected_columns = ["player", "bat_raw", "bat_adj", "ball_raw", "ball_adj", "total"]
    df_filtered = df_filtered[selected_columns]

    # Display results
    if not df_filtered.empty:
        st.write(f"Impact Scores for Match {match_id}")
        st.dataframe(df_filtered)
    else:
        st.warning("No data found for the entered Match ID.")

st.sidebar.write("Built by [Vijay](https://www.linkedin.com/in/vijay-sundaram/)", unsafe_allow_html=True)











