SELECT * FROM students
WHERE 
(quality1 = 'evil' AND quality2 = 'cunning')
OR (quality1 = 'brave' AND quality2 != 'evil')
OR (quality1 in ('studious', 'intelligent') OR quality2 in ('studious', 'intelligent'))
OR (quality1 = 'hufflepuff' OR quality2 = 'hufflepuff')