-- you will be given a table 'kata' with columns 'n', 'x', and 'y'. Return the 'id' and your result in a column named 'res'.
select id, (MOD(k.n, k.y) = 0 and MOD(k.n, k.x) = 0) as res from kata k