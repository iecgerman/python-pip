import utilidades
import read_csv
import charts

def run():
  data =read_csv.read_csv('./data.csv')
  #data = list(filter(lambda item : item['Continent'] == 'South America', data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)


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