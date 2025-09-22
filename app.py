from flask import Flask, render_template

app = Flask(__name__)

# This is a sample list of player data
# In your project, you would replace this with data from the nba_api
sample_players = [
    {'name': 'LeBron James', 'pts': 25.4, 'ast': 7.2, 'reb': 7.6},
    {'name': 'Stephen Curry', 'pts': 27.5, 'ast': 6.3, 'reb': 5.2},
    {'name': 'Kevin Durant', 'pts': 29.1, 'ast': 5.0, 'reb': 7.4},
]

@app.route('/')
def display_players():
    # Renders the players.html template and passes the sample data to it
    # return render_template('players.html', players=sample_players)
    return render_template('homePage.html')

if __name__ == '__main__':
    app.run(debug=True)