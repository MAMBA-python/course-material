-- For 2004 Olympics, generate a list - (birthyear, num-players, num-gold-medals) -
-- containing the years in which the atheletes were born, the number of players
-- born in each of those years who won at least one gold medal, and the number of gold medals
-- won by the players born in that year.

WITH AthensResults AS (
        SELECT r.event_id, r.player_id, p.birthdate, r.medal
        FROM Results r
            JOIN Players p ON p.player_id = r.player_id
            JOIN Events e ON e.event_id = r.event_id
        WHERE e.olympic_id = (SELECT olympic_id FROM Olympics WHERE year=2004) AND r.medal = 'GOLD'
    )
SELECT  EXTRACT(year FROM r.birthdate) as year, count(DISTINCT r.player_id) as players, count(r.medal) as gold_medals
FROM AthensResults r
GROUP BY year, r.medal
ORDER BY year;

