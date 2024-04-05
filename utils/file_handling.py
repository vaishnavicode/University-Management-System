import csv

def read_csv(filename):
    """
    Read data from a CSV file and return it as a list of dictionaries.
    
    Args:
        filename (str): The path to the CSV file.
    
    Returns:
        list: A list of dictionaries, where each dictionary represents a row in the CSV file.
    """
    data = []
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except Exception as e:
        print(f"Error reading {filename}: {e}")
    return data

def write_csv(filename, data):
    """
    Write data to a CSV file.
    
    Args:
        filename (str): The path to the CSV file.
        data (list): A list of dictionaries, where each dictionary represents a row in the CSV file.
    """
    try:
        with open(filename, "w", newline="") as file:
            fieldnames = list(data[0].keys()) if data else []
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"Error writing to {filename}: {e}")
