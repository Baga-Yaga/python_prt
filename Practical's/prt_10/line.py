import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def line_plot():
    x = [1, 2.5, 3, 4, 5]
    y = [10, 12, 8, 15, 10]
    plt.plot(x, y, marker='.')
    plt.title("Line Plot")
    plt.show()

def bar_plot():
    categories = ['A', 'B', 'C', 'D']
    values = [5, 7, 3, 8]
    plt.bar(categories, values, color='skyblue')
    plt.title("Bar Plot")
    plt.show()

def histogram():
    data = np.random.randn(1000)
    plt.hist(data, bins=30, color='purple', edgecolor='black')
    plt.title("Histogram")
    plt.show()

def scatter_plot():
    
    x = np.random.rand(50)
    y = np.random.rand(50)
    colors = np.random.rand(50)
    sizes = 1000 * np.random.rand(50)  # Bubble sizes

    plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
    plt.title("Scatter Plot with Bubble Sizes")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.colorbar()  # Show color scale
    plt.show()

def pie_chart():
    # Sample data
    sizes = [25, 35, 15, 25]
    labels = ['Category A', 'Category B', 'Category C', 'Category D']
    colors = ['gold', 'lightblue', 'lightgreen', 'salmon']

    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title("Pie Chart")
    plt.show()

def box_plot():
    # Sample data
    data = [np.random.normal(0, std, 100) for std in range(1, 4)]

    plt.boxplot(data, vert=True, patch_artist=True, labels=['Set 1', 'Set 2', 'Set 3'])
    plt.title("Box Plot")
    plt.xlabel("Dataset")
    plt.ylabel("Value")
    plt.show()

def heatmap():
    # Sample data
    data = np.random.rand(10, 12)

    sns.heatmap(data, annot=True, cmap='coolwarm', cbar=True)
    plt.title("Heatmap")
    plt.show()

def violin_plot():
    # Sample data
    data = [np.random.normal(0, std, 100) for std in range(1, 4)]

    sns.violinplot(data=data)
    plt.title("Violin Plot")
    plt.xlabel("Dataset")
    plt.ylabel("Value")
    plt.show()

def area_plot():
    # Sample data
    x = range(1, 6)
    y1 = [1, 4, 6, 8, 10]
    y2 = [2, 2, 7, 10, 12]

    plt.fill_between(x, y1, color="skyblue", alpha=0.4, label="Data 1")
    plt.fill_between(x, y2, color="olive", alpha=0.4, label="Data 2")
    plt.title("Area Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.show()

# Example usage
line_plot()
bar_plot()
histogram()
scatter_plot()
pie_chart()
box_plot()
heatmap()
violin_plot()
area_plot()
