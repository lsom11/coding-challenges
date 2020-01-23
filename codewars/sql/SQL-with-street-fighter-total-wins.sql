SELECT 
f.name, 
SUM(f.won) as won, 
SUM(f.lost) as lost
FROM fighters f
LEFT JOIN winning_moves wm ON wm.id = f.move_id
WHERE wm.move NOT IN ('Hadoken', 'Shouoken', 'Kikoken')
GROUP BY f.name
ORDER BY won DESC
LIMIT 6;