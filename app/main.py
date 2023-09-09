import utilidades
import read_csv
import charts
import pandas as pd

def run():
  """  
  #data = list(filter(lambda item : item['Continent'] == 'South America', data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))  
  """
  # df = data frame
  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']

  # OJO aquí con Country/Territory porque en la clase el profe pone sólo Country
  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)

  data =read_csv.read_csv('data.csv')
  country = input('🏴‍☠️  Escribe el pais del cual quieres su poblacion: ')
  print(country)

  resultado = utilidades.population_by_country(data, country)

  if len(resultado) > 0:
    country = resultado[0]
    print(country)
    labels, values = utilidades.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)

  #print(resultado)

if __name__ == '__main__':
  run()