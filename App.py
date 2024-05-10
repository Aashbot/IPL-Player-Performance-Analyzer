import streamlit as st
import pandas as pd
import numpy as np

#########################################
#Batting
class Player1:
    def __init__(self, name, span, matches, innings, not_outs, runs, highest_score, average, balls_faced, strike_rate, centuries, fifties, zeros, fours, sixes):
        self.name = name
        self.span = span
        self.matches = matches
        self.innings = innings
        self.not_outs = not_outs
        self.runs = runs
        self.highest_score = highest_score
        self.average = average
        self.balls_faced = balls_faced
        self.strike_rate = strike_rate
        self.centuries = centuries
        self.fifties = fifties
        self.zeros = zeros
        self.fours = fours
        self.sixes = sixes

    def calculate_score(self):
        # Define weights for each parameter
        weight_matches = 0.1
        weight_innings = 0.1
        weight_not_outs = 0.1
        weight_runs = 0.1
        weight_highest_score = 0.1
        weight_average = 0.1
        weight_balls_faced = 0.05
        weight_strike_rate = 0.1
        weight_centuries = 0.05
        weight_fifties = 0.05
        weight_zeros = 0.05
        weight_fours = 0.05
        weight_sixes = 0.05

        # Calculate performance score
        score = ((self.matches * weight_matches) + (self.innings * weight_innings) + (self.not_outs * weight_not_outs) + (self.runs * weight_runs) + (self.highest_score * weight_highest_score) + (self.average * weight_average) + (self.balls_faced * weight_balls_faced) + (self.strike_rate * weight_strike_rate) + (self.centuries * weight_centuries) + (self.fifties * weight_fifties) - (self.zeros * weight_zeros) + (self.fours * weight_fours) + (self.sixes * weight_sixes))/10
        rounded_score1 = round(score, 2)
        return rounded_score1
    
def calculate_batting_scores(data):
    relevant_columns = ["Player", "Span", "Mat", "Inns", "NO", "Runs", "HS", "Ave", "BF", "SR", "100", "50", "0", "4s", "6s"]
    data = data[relevant_columns]
    players_data = data.to_dict(orient='records')
    players = [Player1(name=player_data["Player"], span=player_data["Span"], matches=player_data["Mat"], innings=player_data["Inns"], not_outs=player_data["NO"], runs=player_data["Runs"], highest_score=player_data["HS"], average=player_data["Ave"], balls_faced=player_data["BF"], strike_rate=player_data["SR"], centuries=player_data["100"], fifties=player_data["50"], zeros=player_data["0"], fours=player_data["4s"], sixes=player_data["6s"]) for player_data in players_data]
    player_scores = [(player.name, player.calculate_score()) for player in players]
    return player_scores
    


#Batting
#############################################################

#############################################################

#############################################################
#FIELDING
class Player2:
    def __init__(self, name, span, matches, innings, dismissals, catches, stumpings, catches_wk, catches_field, matches_dismissals, dismissal_innings_ratio):
        self.name = name
        self.span = span
        self.matches = matches
        self.innings = innings
        self.dismissals = dismissals
        self.catches = catches
        self.stumpings = stumpings
        self.catches_wk = catches_wk
        self.catches_field = catches_field
        self.matches_dismissals = matches_dismissals
        self.dismissal_innings_ratio = dismissal_innings_ratio

    def calculate_score(self):
        # Define weights for each parameter
        weight_matches = 0.1
        weight_innings = 0.1
        weight_dismissals = 0.2
        weight_catches = 0.1
        weight_stumpings = 0.1
        weight_catches_wk = 0.2
        weight_catches_field = 0.2
        #weight_matches_dismissals = 0.1
        #weight_dismissal_innings_ratio = 0.1

        # Calculate performance score
        score = (self.matches * weight_matches) + (self.innings * weight_innings) + (self.dismissals * weight_dismissals) + (self.catches * weight_catches) + (self.stumpings * weight_stumpings) + (self.catches_wk * weight_catches_wk) + (self.catches_field * weight_catches_field) # (self.matches_dismissals * weight_matches_dismissals) 
        #(self.dismissal_innings_ratio * weight_dismissal_innings_ratio)
        rounded_score2 = round(score, 2)
        return rounded_score2
    
def calculate_fielding_scores(data):
    relevant_columns = ["Player", "Span", "Mat", "Inns", "Dis", "Ct", "St", "Ct Wk", "Ct Fi", "MD", "D/I"]
    data = data[relevant_columns]
    players_data = data.to_dict(orient='records')
    players = [Player2(name=player_data["Player"], span=player_data["Span"], matches=player_data["Mat"], innings=player_data["Inns"], dismissals=player_data["Dis"], catches=player_data["Ct"], stumpings=player_data["St"], catches_wk=player_data["Ct Wk"], catches_field=player_data["Ct Fi"], matches_dismissals=player_data["MD"], dismissal_innings_ratio=player_data["D/I"]) for player_data in players_data]
    player_scores = [(player.name, player.calculate_score()) for player in players]
    return player_scores



#FIELDING
#############################################################

#############################################################

#############################################################
#Bowling
class Player3:
    def __init__(self, name, span, matches, innings, runs, average, strike_rate, overs, maidens, wickets, best_bowling, economy, fours_wickets, fives_wickets):
        self.name = name
        self.span = span
        self.matches = matches
        self.innings = innings
        self.runs = runs
        self.average = average
        self.overs = overs
        self.maidens = maidens
        self.wickets = wickets
        self.best_bowling = best_bowling
        self.economy = economy
        self.strike_rate = strike_rate
        self.fours_wickets = fours_wickets
        self.fives_wickets = fives_wickets

    def calculate_score(self):
        weight_matches = 0.1
        weight_innings = 0.1
        weight_runs = 0.1
        weight_average = 0.1
        weight_overs = 0.1
        weight_maidens = 0.1
        weight_wickets = 0.1
        weight_economy = 0.1
        weight_strike_rate = 0.1
        weight_fours_wickets = 0.05
        weight_fives_wickets = 0.05

        score = ((self.matches * weight_matches) + (self.innings * weight_innings) + (self.runs * weight_runs) + (self.average * weight_average) + (self.overs * weight_overs) + (self.maidens * weight_maidens) + (self.wickets * weight_wickets) + (self.economy * weight_economy) + (self.strike_rate * weight_strike_rate) + (self.fours_wickets * weight_fours_wickets) + (self.fives_wickets * weight_fives_wickets))/10
        rounded_score3 = round(score, 2)
        return rounded_score3


def calculate_bowling_scores(data):
    relevant_columns = ["Player", "Span", "Mat", "Inns", "Overs", "Mdns", "Runs", "Wkts", "BBI", "Ave", "Econ", "SR", "4", "5"]
    data = data[relevant_columns]
    players_data = data.to_dict(orient='records')
    players = [Player3(name=player_data["Player"], span=player_data["Span"], matches=player_data["Mat"], innings=player_data["Inns"], overs=player_data["Overs"], maidens=player_data["Mdns"], runs=player_data["Runs"], wickets=player_data["Wkts"], best_bowling=player_data["BBI"], average=player_data["Ave"], economy=player_data["Econ"], strike_rate=player_data["SR"], fours_wickets=player_data["4"], fives_wickets=player_data["5"]) for player_data in players_data]
    player_scores = [(player.name, player.calculate_score()) for player in players]
    return player_scores

#Bowling
#############################################################

#############################################################

#############################################################
#All rounder 
def calculate_all_rounder_scores(batting_scores, fielding_scores, bowling_scores):
    all_rounder_scores = {}
    for player_name, batting_score in batting_scores:
        if player_name in all_rounder_scores:
            all_rounder_scores[player_name] += batting_score
        else:
            all_rounder_scores[player_name] = batting_score
    
    for player_name, fielding_score in fielding_scores:
        if player_name in all_rounder_scores:
            all_rounder_scores[player_name] += fielding_score
        else:
            all_rounder_scores[player_name] = fielding_score
    
    for player_name, bowling_score in bowling_scores:
        if player_name in all_rounder_scores:
            all_rounder_scores[player_name] += bowling_score
        else:
            all_rounder_scores[player_name] = bowling_score

    rounded_all_rounder_scores = {player_name: round(score, 2) for player_name, score in all_rounder_scores.items()}
    return list(rounded_all_rounder_scores.items())

#All rounder
#############################################################

#############################################################

#############################################################


# Display results using Streamlit
#st.write("Below are the performance scores for each player based on their bowling statistics:")

#for name, score in player_scores:
    #st.write(f"{name}: {score}")
st.set_page_config(page_title="Player Effectiveness for IPL Auction", page_icon=":cricket:", layout="wide")
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            .stDeployButton {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def main():
    st.title("Player Effectiveness for IPL Auction")

    # Create a dropdown menu for selecting data type
    data_type = st.selectbox("Select data type:", ["Batting", "Fielding", "Bowling", "All Rounder"])

    if data_type == "Batting":
        data = pd.read_csv("t20.csv",na_values=['','-'])
        player_scores = calculate_batting_scores(data)
        # Display batting scores
        display_scores_with_images(player_scores, data, data_type)
        
    elif data_type == "Fielding":
        data = pd.read_csv("Fielding_t20.csv",na_values=['','-'])
        player_scores = calculate_fielding_scores(data)
        # Display fielding scores
        display_scores_with_images(player_scores, data, data_type)
        
    elif data_type == "Bowling":
        data = pd.read_csv("Bowling_t20.csv",na_values=['','-'])
        player_scores = calculate_bowling_scores(data)
        # Display bowling scores
        display_scores_with_images(player_scores, data, data_type)
        
    elif data_type == "All Rounder":
        batting_data = pd.read_csv("t20.csv", na_values=['', '-'])
        fielding_data = pd.read_csv("Fielding_t20.csv", na_values=['', '-'])
        bowling_data = pd.read_csv("Bowling_t20.csv", na_values=['', '-'])
        
        batting_scores = calculate_batting_scores(batting_data)
        fielding_scores = calculate_fielding_scores(fielding_data)
        bowling_scores = calculate_bowling_scores(bowling_data)
        
        player_scores = calculate_all_rounder_scores(batting_scores, fielding_scores, bowling_scores)
        # Display all rounder scores
        display_all_rounder_scores_with_images(player_scores, batting_data, fielding_data, bowling_data)

def display_scores_with_images(player_scores, data, data_type):
    # Display the results
    search_query = st.text_input("Search for a player:")
    if search_query:
        search_result = [player for player in player_scores if search_query.lower() in player[0].lower()]
        if search_result:
            st.write(f"**Search results for '{search_query}':**")
            for name, score in search_result:
                st.markdown(f"### **{name}: {score}**")
                if data_type == "Batting":
                    image_path = data[data['Player'] == name]['Image_Path'].values
                elif data_type == "Fielding":
                    image_path = data[data['Player'] == name]['Image_Path'].values
                elif data_type == "Bowling":
                    image_path = data[data['Player'] == name]['Image_Path'].values
                if len(image_path) and not (isinstance(image_path[0], float) and np.isnan(image_path[0])):
                    st.image(image_path[0], caption=name, width=512)
                else:
                    st.write("")
        else:
            st.write(f"No player found matching '{search_query}'")

def display_all_rounder_scores_with_images(player_scores, batting_data, fielding_data, bowling_data):
    # Combine all DataFrames into one
    all_data = pd.concat([batting_data, fielding_data, bowling_data], axis=0)
    
    # Display the results
    search_query = st.text_input("Search for a player:")
    if search_query:
        search_result = [player for player in player_scores if search_query.lower() in player[0].lower()]
        if search_result:
            st.write(f"Search results for '{search_query}':")
            for name, score in search_result:
                st.markdown(f"### **{name}: {score}**")
                if not np.isnan(score):
                    image_path = all_data[all_data['Player'] == name]['Image_Path'].values
                    if len(image_path) > 0 and not (isinstance(image_path[0], float) and np.isnan(image_path[0])):
                        st.image(image_path[0], caption=name, width=512)
                    else:
                        st.write("Image not found.")
        else:
            st.write(f"No player found matching '{search_query}'")


if __name__ == "__main__":
    main()
