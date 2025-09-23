Follow these steps to build and run the application using Docker. Docker can be downloaded from the [Docker website](https://www.docker.com).

1.  **Build the Docker Image**:
        Navigate to the project's root directory in your terminal and run the following command to build the Docker image.

```bash
docker build -t nba-stats-app .
```

2.  **Run the Container**:
        Once the image is built, you can run the application in a Docker container.

```bash
docker run -p 5001:5000 nba-stats-app
```

The application will be available at `http://localhost:5001`.

Currently, my plan is to make an api that uses data scraped by swar's nba api - https://github.com/swar/nba_api - and using that data I'll make some sort of gui display that allows you to interact with the stats.

The levels I'm thinking of appraoching this project:

1st level:
- Create a webpage front end for the data
- The page will allow you to navigate through all the teams in the league, checking their stats etc

2nd level:
- Implement a feature that allows you to compare two players stats side by side with a nice UI

3rd level:
- Train a ML model to go through the data and predict a player's stats for a game