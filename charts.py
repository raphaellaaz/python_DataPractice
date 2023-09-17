import matplotlib.pyplot as plot
from practice_csv import data_to_charts, world_populations

def generate_bar_chart(labels, values):
    fig, ax = plot.subplots()
    ax.bar(labels, values)
    plot.show()

def generate_pie_chart(diccionarioWorld):
    frec=diccionarioWorld.values()
    label=diccionarioWorld.keys()
    plot.figure(figsize=(6,6))
    plot.pie(frec, labels=label, autopct='%1.2f%%', startangle=90)
    plot.title("World Population")
    plot.show()

if __name__=='__main__':
    pais = input('Ingresa el Pais a Consultar ==>> ')
    pais= pais.capitalize()
    labels, values = data_to_charts(pais,'./world.csv')
    # generate_bar_chart(labels, values)
    generate_pie_chart(world_populations('./world.csv'))