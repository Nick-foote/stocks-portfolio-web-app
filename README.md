# stocks-portfolio-web-app
A web app to track stock ticker information and price. Then using Dash apps the information is graphed with multiple tickers in an interactive graphic. 



## Plotly Dash (with Django)

Creates an interactive dashboard where you can select the dates and stocks to compare the share price history.
Share price information is gathered from Yahoo through the Pandas Data Reader tool. By using Plotly Dash, the user can hover and interact with each stock, updating the tickers live.

<img width="1000" alt="graph_dashboard" src="https://user-images.githubusercontent.com/68865367/98394324-778bf480-2052-11eb-95b3-c80cc57f9b5d.png">




Users can also add & remove  stocks to a table of their favourites to easily have on hand.

<img width="1000" alt="stock_favourites" src="https://user-images.githubusercontent.com/68865367/98394334-7c50a880-2052-11eb-8a6f-94d48a965ce8.png">




Individual information about the company and share data can be looked up, which is connected to the IEX API for the latest company information.

<img width="1000" alt="stock_lookup" src="https://user-images.githubusercontent.com/68865367/98394340-7fe42f80-2052-11eb-8bac-df457eeb1ae1.png">
