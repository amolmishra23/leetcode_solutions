# Write your MySQL query statement below
SELECT s.Score as score, dense_rank() over(order by Score DESC) as 'Rank'
FROM Scores s;