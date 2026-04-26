import matplotlib.pyplot as plt

def bar_chart(data):
    data.plot(kind='bar')
    plt.show()

def line_chart(data):
    data.plot(kind='line')
    plt.show()

def pie_chart(data):
    data.plot(kind='pie')
    plt.show()

def histogram(data):
    data.plot(kind='hist')
    plt.show()