from data_connector.csv_data_connector import CSVDataConnector

csvdp = CSVDataConnector('data/movies.csv')
dupa = csvdp.load_data()

for i in dupa:
    print(i)
