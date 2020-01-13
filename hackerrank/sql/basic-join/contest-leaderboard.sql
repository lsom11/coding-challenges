SELECT h.hacker_id, h.name, sum(score) as total_score
    FROM Hackers as h 
    INNER JOIN (select hacker_id,  max(score) as score from submissions group by challenge_id, hacker_id) max_score
    ON h.hacker_id=max_score.hacker_id
    GROUP BY h.hacker_id, name
    HAVING total_score > 0
ORDER BY total_score DESC, h.hacker_id;