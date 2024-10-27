# This is an interactive data application that features a dashboard displaying a histogram and scatterplot for selected datasets. 

# Users can modify specific aspects of the visuals and see the results in real-time. 

# This data application consists of two components: the user interface and the server section. 

# The user interface enables users to issue commands that are executed on the server side.



# Import the required dependencies

import matplotlib.pyplot as plt

import numpy as np

import seaborn as sns

from palmerpenguins import load_penguins

from shiny.express import input, render, ui



# Add page options for the overall app.

ui.page_opts(title="Pyshiny Plot App by DataHub", fillable=True)



# Create a sidebar with a slider input and input selector.

with ui.sidebar():

    # Slider for specifying the number of bins in the histogram.

    ui.input_slider("selected_number_of_bins", "Number of Bins", 5, 50, 25)

    

    # Selector for specifying which penguin species to be observed.

    ui.input_select("Species", "Species of Choice", ["Adelie", "Chinstrap", "Gentoo"])



@render.plot(alt="A histogram showing random data distribution and scatterplot for Palmer Penguin")

def draw_histogram():

    # Define the number of points to generate.

    count_of_points = 437

    # Set a random seed to ensure reproducibility of the same results.

    np.random.seed(10)

    

    # Generate random data.

    random_data_array = 100 + 18 * np.random.randn(count_of_points)

    

    # Create a histogram for the randomly generated dataset.

    plt.hist(random_data_array, input.selected_number_of_bins(), density=True)

    plt.title("Histogram of Random Data")

    plt.xlabel("Value")

    plt.ylabel("Density")

    plt.grid(True)



@render.plot(alt="A scatterplot for Palmer Penguin species")

def draw_scatterplot():

    penguins = load_penguins()

    penguins_species = penguins[penguins["species"] == input.Species()]

    

    # Ensure the spelling of the column is correct

    sns.scatterplot(x="bill_length_mm", y="body_mass_g",hue ='species',data=penguins_species)

    plt.title(f"Scatterplot for {input.Species} Penguins")

    plt.xlabel("Bill Length (mm)")

    plt.ylabel("Body Mass (g)")

    plt.grid(True)
