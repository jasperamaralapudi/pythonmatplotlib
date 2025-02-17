import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]

bars = plt.bar(categories, values, color='skyblue')
plt.title("Bar Plot with Annotations")
plt.xlabel("Categories")
plt.ylabel("Values")

# Add annotations
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height}', ha='center', va='bottom')

plt.show()