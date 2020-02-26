SELECT id, name, POSITION(',' in characteristics) comma
FROM monsters
ORDER BY comma;