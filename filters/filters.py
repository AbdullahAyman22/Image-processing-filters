import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from median_min_max_filters import median_min_max_filters
from histogram_equalization import histogram_equalization
from zoom_nearest_neighbour import zoom_nearest_neighbour
from correlation import correlation
from zoom_bilinear import zoom_bilinear
from convolution import convolution


import numpy as np
import cv2

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)  # Read image in grayscale using cv2
        return img

def load_and_display_image():
    global original_image
    original_image = open_image()

    original_tk = ImageTk.PhotoImage(image=Image.fromarray(original_image))

    original_label.config(image=original_tk)
    original_label.image = original_tk

def apply_filter():
    selected_filter = filter_var.get()
    if selected_filter == "zoom_nearest_neighbour":
        img_array = np.array(original_image)
        iterations = iterations_var.get()
        equalized_array = zoom_nearest_neighbour(img_array,iterations)
        equalized_image = Image.fromarray(equalized_array)

        equalized_tk = ImageTk.PhotoImage(image=equalized_image)

        filtered_label.config(image=equalized_tk)
        filtered_label.image = equalized_tk

    elif selected_filter == "zoom_bilinear":
        img_array = np.array(original_image)
        iterations = iterations_var.get()
        equalized_array = zoom_bilinear(img_array,iterations)
        equalized_image = Image.fromarray(equalized_array)

        equalized_tk = ImageTk.PhotoImage(image=equalized_image)

        filtered_label.config(image=equalized_tk)
        filtered_label.image = equalized_tk

    elif selected_filter == "Histogram Equalization":
        img_array = np.array(original_image)
        equalized_array = histogram_equalization(img_array)
        equalized_image = Image.fromarray(equalized_array)

        equalized_tk = ImageTk.PhotoImage(image=equalized_image)

        filtered_label.config(image=equalized_tk)
        filtered_label.image = equalized_tk

    elif selected_filter == "Correlation":

        selected_filter = filter_var.get()
    
    # Get the values from the array input fields and convert to a 2D array
        filter_array = []
        for row in array_input:
            row_values = []
            for entry in row:
                value = entry.get()
                row_values.append(float(value))
            filter_array.append(row_values)
        
        # Convert the list of lists to a numpy array
        filter_array = np.array(filter_array)
        
        
        img_array = np.array(original_image)
        equalized_array = correlation(img_array,filter_array)
        equalized_image = Image.fromarray(equalized_array)

        equalized_tk = ImageTk.PhotoImage(image=equalized_image)

        filtered_label.config(image=equalized_tk)
        filtered_label.image = equalized_tk
    
    elif selected_filter == "Convolution":

        selected_filter = filter_var.get()
    
    # Get the values from the array input fields and convert to a 2D array
        filter_array = []
        for row in array_input:
            row_values = []
            for entry in row:
                value = entry.get()
                row_values.append(float(value))
            filter_array.append(row_values)
        
        # Convert the list of lists to a numpy array
        filter_array = np.array(filter_array)
        
        
        img_array = np.array(original_image)
        equalized_array = convolution(img_array,filter_array)
        equalized_image = Image.fromarray(equalized_array)

        equalized_tk = ImageTk.PhotoImage(image=equalized_image)

        filtered_label.config(image=equalized_tk)
        filtered_label.image = equalized_tk
    
    else:
        num = 4 if selected_filter == "Median" else 8 if selected_filter == "Max" else 0 if selected_filter == "Min" else 1 if selected_filter == "Average" else 2

        img_array = np.array(original_image)
        iterations = iterations_var.get()

        filtered_array = median_min_max_filters(img_array, num, iterations)
        filtered_image = Image.fromarray(filtered_array)

        filtered_tk = ImageTk.PhotoImage(image=filtered_image)

        filtered_label.config(image=filtered_tk)
        filtered_label.image = filtered_tk




root = tk.Tk()
root.title("Image Filter App")

root.attributes("-fullscreen", True)  
root.title("Image Filter App")

close_button = tk.Button(root, text="Close", command=root.destroy)
close_button.grid(row=0, column=0, columnspan=2)

# Create and grid GUI elements
filter_var = tk.StringVar()
filter_dropdown = ttk.Combobox(root, textvariable=filter_var, values=["Median", "Max", "Min","Average","Gaussian","Histogram Equalization","zoom_nearest_neighbour","zoom_bilinear","Correlation","Convolution"])
filter_dropdown.grid(row=1, column=0, columnspan=2)

root.attributes("-fullscreen", True)

original_label = tk.Label(root)
original_label.grid(row=2, column=0)

filtered_label = tk.Label(root)
filtered_label.grid(row=2, column=1)

load_button = tk.Button(root, text="Load Image", command=load_and_display_image)
load_button.grid(row=3, column=0, columnspan=2)

apply_button = tk.Button(root, text="Apply Filter", command=apply_filter)
apply_button.grid(row=4, column=0, columnspan=2)

iterations_label = tk.Label(root, text="Iterations:")
iterations_label.grid(row=5, column=0, columnspan=2)

iterations_var = tk.IntVar(value=1)
iterations_slider = tk.Scale(root, from_=1, to=5, variable=iterations_var, orient="horizontal")
iterations_slider.grid(row=6, column=0, columnspan=2)

array_input_label = tk.Label(root, text="Enter 3x3 Array:")
array_input_label.grid(row=7, column=0, columnspan=2)

array_input = []
for i in range(3):
    row = []
    for j in range(3):
        entry = tk.Entry(root)
        entry.grid(row=9 + i, column=j+1)
        row.append(entry)
    array_input.append(row)


original_image = None




root.mainloop()
