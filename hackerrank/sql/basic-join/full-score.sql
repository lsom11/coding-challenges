SELECT h.hacker_id, h.name FROM Submissions s
  INNER JOIN Challenges c ON c.challenge_id = s.challenge_id
  INNER JOIN Hackers h ON h.hacker_id = s.Hacker_id
  INNER JOIN Difficulty d on c.difficulty_level = d.difficulty_level
  WHERE s.score = d.score AND c.difficulty_level = d.difficulty_level
  GROUP BY h.hacker_id, h.name
  HAVING COUNT(s.hacker_id) > 1
  ORDER BY COUNT(s.hacker_id) DESC, s.hacker_id ASC