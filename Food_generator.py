import tkinter as tk    
import requests
from urllib.request import urlopen
from PIL import Image
from pprint import pprint   #printing module



api_key = '1'

# API endpoint for searching meals by name
search_url_byMname = f'https://www.themealdb.com/api/json/v1/{api_key}/search.php'


#not using following apis only for reference 
'''
#API endpoint for searching be ingredients 
filter_by_ingredient_url = f'https://www.themealdb.com/api/json/v1/{api_key}/filter.php'      


#RapidAPI
url_fromRapidAPI = "https://food-recipes-with-images.p.rapidapi.com/"
'''


#Takes meal name as argument, constructs a dictionary('params') with search term
#Then sends Get request to the specified API endpoint (searc_url')
# If the response status code is 200 (OK), it parses the JSON response 
# and returns the data. Otherwise, it prints an error message and returns None.

def search_meal_by_name(meal_name):
    params = {'s': meal_name}
    response = requests.get(search_url_byMname, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        
        
        return data
        
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None



#when search is clicked
def on_search_button_click():
    meal_name = entry.get()
    search_result = search_meal_by_name(meal_name)
    
    if search_result:
        result_text.delete(1.0, tk.END)  # Clear previous results
        result_text.insert(tk.END, str(pprint(search_result)))

   
   
#clear is clicked
def on_clear_button_click():

   result_text.delete(1.0, tk.END)  # Clear previous results
        


root = tk.Tk()
root.title("Flavour Fusion") # root window title and dimension
root.geometry('600x500') 
 
#Title Label
title_label = tk.Label(root, text="Welcome to Flavour Fusion!", font=("Chiller", 36, "bold"))
title_label.pack(pady=10)


# User Instructions Label
instructions_label = tk.Label(root, text="Enter a main ingredient or Food to search:")
instructions_label.pack(pady=10)

# Entry Widget
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

#where txt is being displayed
# Create result_text as a Tkinter Text widget                #probably edit this part 
result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=10)


#Search Button
generate_button = tk.Button(root, text="Search", command=on_search_button_click)
generate_button.pack(pady=10)


#Clear Button
Clear_button = tk.Button(root, text="Clear", command=on_clear_button_click)
Clear_button.pack(pady=10)


# Result Label (will be updated when the generate button is clicked)
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Execute Tkinter
root.mainloop()

