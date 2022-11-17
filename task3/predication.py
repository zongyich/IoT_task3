from ml_engine import MLPredictor
import json
import pandas as pd

if __name__ == '__main__':
    # Prepare data

    f = open('data.json')
    data_dict = json.load(f)
    f.close();

    data_list = data_dict['date']
    date = []
    value = []

    for item in data_list:
        date.append(item['Date'])
        value.append(item['Value'])
        
    data = {
         'Timestamp': date,
        'Value': value
    }
    data_df = pd.DataFrame(data)

    # Create ML engine predictor object
    predictor = MLPredictor(data_df)
    # Train ML model
    predictor.train()
    # Do prediction
    forecast = predictor.predict()

	# Get canvas
    fig = predictor.plot_result(forecast)
    fig.savefig("prediction.png")
    fig.show()
