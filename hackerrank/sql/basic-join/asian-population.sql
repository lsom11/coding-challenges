SELECT SUM(city.population)
FROM city
  INNER JOIN country ON country.code = city.countrycode
WHERE country.continent = 'Asia'