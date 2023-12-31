import json

# Open the text file containing the URLs
with open('urls.txt', 'r') as file:
    url_list = file.read()

# Split the lines into individual URLs
urls = url_list.strip().split('\n')

# Create a JSON array containing only the URLs
json_array = urls

# Save the JSON array to a file
with open('urls.json', 'w') as json_file:
    json.dump(json_array, json_file)

print("JSON array has been written to the file 'urls.json'.")
