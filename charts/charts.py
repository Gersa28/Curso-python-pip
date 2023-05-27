import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 54, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('./chart_pie.png')
    plt.close()