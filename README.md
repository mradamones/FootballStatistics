# Application to manage football stats from fbref.com
This app was part of my diploma thesis. I implemented ingesting data from fbref.com (players stats form top 5 leagues)
 and every user can view tables with goalkeeper stats, field players and based on formation).
Entire app was written in Python (frontend: PyQt6; backend: Pandas, NumPy, Pickle, scikit-learn; plots: Plotly Express)

### Data ingest
Using Pandas all 11 tables are ingested and then unnecessary columns and rows are deleted. Next appropiate views are created and passed to application.
To lower website traffic tables are saved to files using Pickle library (user can choose whether he wants to download data or load from files).
[Fbref.com](https://www.sports-reference.com/bot-traffic.html) defines policies of requesting data. App sends only 11 requests once per instance of program, so there should not be possibility to break rule of maximum 20 requests per minute.

### Finding similar players
App finds the most similar player to selected one using one of 5 algorithms:
- Manhattan similarity
- euclidean distance
- Pearson correlation
- mean average (naive algorithm that finds minimal gap between arithmetic averages of every players stats)
- cosine similarity

As a result, in window appears all stats of chosen player and found "twin") - in plans is to add label with similarity level in percents

### Classificator
Machine learning algorithms were implemented to guess player position (defender, midfielder, forward - only main position) basing on stats.
Like in previous section, user select player by double-click on any cell in row and select preferred model.
Models differ in algorithms used to train them. User can choose between:
- KNeighbours Classifier
- SVC (Support Vector Machine)
- Random Forest Classifier
- Gaussian NB
- Multi-Layer Perceptron
- Decision Tree Classifier

All algorithms are from _scikit-learn_ library. Models were tested using GridSearchCV (results - best parameters and highest achieved accuracy - are in [classes.py](./classificator/classes.py) file).

### Radar diagrams
In diagrams section user can - of course - select player by double-clicking him. Next step is to select stats to present (between 3 and 8). 
Stats available depends on selected dataset (between goalkeepers and field players).
Plot will be shown in web browser in new card. Values are scaled to range [0;1], where 1 is highest value for a column in entire dataset (to repair in the future).


Library used for plotting: Plotly Express