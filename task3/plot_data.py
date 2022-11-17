import json
import matplotlib.pyplot as plt
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

    # Initialize a canvas
    plt.figure(figsize=(8, 4), dpi=200)
    # Plot data into canvas
    plt.plot(data_df["Timestamp"], data_df["Value"], color="#FF3B1D", marker='.', linestyle="-")
    plt.title("Example data for demonstration")
    plt.xlabel("DateTime")
    plt.ylabel("Value")

    # Save as file
    plt.savefig("figure1.png")
    # Directly display
    plt.show()
