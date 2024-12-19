import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from median_min_max_filters import median_min_max_filters
import numpy as np
import cv2

####

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path).convert("L")  # Convert to grayscale
        return img

def load_and_display_image():
    global original_image
    original_image = open_image()

    original_tk = ImageTk.PhotoImage(original_image)

    original_label.config(image=original_tk)
    original_label.image = original_tk

def apply_filter():
    selected_filter = filter_var.get()
    num = 4 if selected_filter == "Median" else 8 if selected_filter == "Max" else 0

    img_array = np.array(original_image)
    iterations = iterations_var.get()  # Get the selected number of iterations

    filtered_array = median_min_max_filters(img_array, num, iterations)  # Pass the iterations
    filtered_image = Image.fromarray(filtered_array)

    filtered_tk = ImageTk.PhotoImage(filtered_image)

    filtered_label.config(image=filtered_tk)
    filtered_label.image = filtered_tk

# Create the main window
root = tk.Tk()
root.title("Image Filter App")

# Create GUI elements
filter_var = tk.StringVar()
filter_dropdown = ttk.Combobox(root, textvariable=filter_var, values=["Median", "Max", "Min"])
filter_dropdown.grid(row=0, column=0, columnspan=2)

original_label = tk.Label(root)
original_label.grid(row=1, column=0)

filtered_label = tk.Label(root)
filtered_label.grid(row=1, column=1)

load_button = tk.Button(root, text="Load Image", command=load_and_display_image)
load_button.grid(row=2, column=0, columnspan=2)

apply_button = tk.Button(root, text="Apply Filter", command=apply_filter)
apply_button.grid(row=3, column=0, columnspan=2)

# Slider for iterations
iterations_label = tk.Label(root, text="Iterations:")
iterations_label.grid(row=4, column=0, columnspan=2)

iterations_var = tk.IntVar(value=1)
iterations_slider = tk.Scale(root, from_=1, to=5, variable=iterations_var, orient="horizontal")
iterations_slider.grid(row=5, column=0, columnspan=2)

# Store the loaded image
original_image = None

# Start the Tkinter event loop
root.mainloop()
