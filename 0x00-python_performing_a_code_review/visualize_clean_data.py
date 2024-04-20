#!/usr/bin/env python3
"""Visualize Clean Data
"""
def column_to_label(column_name):
    """
    Converts a column name in a pandas DataFrame to a string that can be
    used as a label in a plot.
    
    :param column_name: string containing original column name
    :return: string that is ready to be presented on a plot
    """
    
    if isinstance(column_name, str):
        return " ".join(column_name.split("_")).title()
        # Update 5: Encapsulated logic into 'column_to_label' function to promote DRY principle.
    else:
        raise Exception("Column name must be a string.")

def visualize_versus_price(clean_data, x):
    """
    Use seaborn and matplotlib to identify a pattern between avg_rating and 
    battery_capacity.
    
    :param clean_data: a pandas DataFrame containing cleaned smartphone data
    :param x: variable to be plotted on the x-axis
    :return: None
    """
    
    x_title = column_to_label(x)
    # Update 6: Used 'column_to_label' function to remove duplicated code.
    
    sns.scatterplot(x=x, y="price", data=clean_data, hue="os")
    plt.xlabel(x_title)
    plt.ylabel("Price ($)")
    plt.title(f"{x_title} vs. Price")

# Visualize the data
visualize_versus_price(cleaned_data, "processor_speed")
