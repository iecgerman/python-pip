import matplotlib.pyplot as plt

def generate_pie_chart():
    
    labels = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    values = [5500, 23452, 65225, 6521, 3796, 500, 6500, 51744, 9399, 26524, 5834, 500]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()

