import json
import os

def load_data(filename='data.json'):
    file_path = os.path.join(os.path.dirname(__file__), filename)
    
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {filename}.")
        return []

if __name__ == "__main__":
    restaurants_data = load_data()
    print("Restaurants Loaded Successfully! Number of entries:", len(restaurants_data))
