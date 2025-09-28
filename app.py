from flask import Flask, render_template
from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonteamroster
from flask_livereload import LiveReload

app = Flask(__name__)
LiveReload(app)

# ----------------- NEW: Position Mapping Dictionary -----------------
# This maps the abbreviations (C, F, G) to their full names.
POSITION_MAP = {
    'C': 'Center',
    'F': 'Forward',
    'G': 'Guard',
    'C-F': 'Center-Forward',
    'F-C': 'Forward-Center',
    'F-G': 'Forward-Guard',
    'G-F': 'Guard-Forward',
    'G-C': 'Guard-Center'
}
# --------------------------------------------------------------------

# A mapping from URL slugs to the team's official full name
# ... (rest of your team_name_map dictionary) ...
team_name_map = {
    'celtics': 'Boston Celtics',
    'raptors': 'Toronto Raptors',
    'sixers': 'Philadelphia 76ers',
    'nets': 'Brooklyn Nets',
    'knicks': 'New York Knicks',
    'pacers': 'Indiana Pacers',
    'bucks': 'Milwaukee Bucks',
    'bulls': 'Chicago Bulls',
    'pistons': 'Detroit Pistons',
    'cavaliers': 'Cleveland Cavaliers',
    'heat': 'Miami Heat',
    'hornets': 'Charlotte Hornets',
    'wizards': 'Washington Wizards',
    'magic': 'Orlando Magic',
    'hawks': 'Atlanta Hawks',
    'nuggets': 'Denver Nuggets',
    'thunder': 'Oklahoma City Thunder',
    'jazz': 'Utah Jazz',
    'blazers': 'Portland Trail Blazers',
    'timberwolves': 'Minnesota Timberwolves',
    'lakers': 'Los Angeles Lakers',
    'clippers': 'Los Angeles Clippers',
    'suns': 'Phoenix Suns',
    'kings': 'Sacramento Kings',
    'warriors': 'Golden State Warriors',
    'rockets': 'Houston Rockets',
    'mavericks': 'Dallas Mavericks',
    'grizzlies': 'Memphis Grizzlies',
    'spurs': 'San Antonio Spurs',
    'pelicans': 'New Orleans Pelicans',
}


# Get all NBA teams once when the app starts
nba_teams = teams.get_teams()

# Create a dictionary to map full team names to their official team ID
team_name_to_id = {
    team['full_name']: team['id'] 
    for team in nba_teams
}

@app.route('/')
def home_page():
    return render_template('homePage.html')

# This is a dynamic route that takes a team name slug
@app.route('/team/<team_name_slug>')
def team_page(team_name_slug):
    # Get the official team name from the map using the slug
    full_team_name = team_name_map.get(team_name_slug)
    
    # If the slug is in our map, get the corresponding ID
    if full_team_name:
        team_id = team_name_to_id.get(full_team_name)
    else:
        team_id = None

    # If a team ID is found, fetch the roster
    if team_id:
        try:
            # Use the commonteamroster endpoint to get the team's roster
            roster_data = commonteamroster.CommonTeamRoster(team_id=team_id)
            players_df = roster_data.get_data_frames()[0]

            players = players_df[['PLAYER_ID', 'PLAYER', 'NUM', 'POSITION', 'HEIGHT', 'WEIGHT', 'AGE']].to_dict('records')

            # ----------------- MODIFIED: Translate position abbreviations -----------------
            for player in players:
                abbreviation = player['POSITION']
                # Use .get() to safely retrieve the full name, or use the original abbreviation if not found
                player['POSITION'] = POSITION_MAP.get(abbreviation, abbreviation)
            # ------------------------------------------------------------------------------

            # Pass the team name and player data to the template
            return render_template('players.html', players=players, team=full_team_name)
        except Exception as e:
            # Handle potential API errors
            return f"An error occurred: {e}", 500
    else:
        # Handle cases where the team name isn't found
        return "Team not found", 404

if __name__ == '__main__':
    app.run(debug=True)