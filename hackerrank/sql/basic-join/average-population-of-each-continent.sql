SELECT country.continent,
  floor(avg(city.population))
FROM city
  JOIN country ON country.code = city.countrycode
GROUP BY country.CONTINENT