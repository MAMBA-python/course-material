-- Find all athletes who won at least one of each medal (GOLD, SILVER and
-- BRONZE) at a single Olympics. Report as -- "(player-name, olympic-id)".

WITH PlayerMedals AS (
        SELECT p.name, e.olympic_id,
               count(CASE WHEN r.medal = 'GOLD' THEN 1 END) as gold,
               count(CASE WHEN r.medal = 'SILVER' THEN 1 END) as silver,
               count(CASE WHEN r.medal = 'BRONZE' THEN 1 END) as bronze
        FROM Results r
            JOIN Events e on e.event_id = r.event_id
            JOIN Players p on p.player_id = r.player_id
        GROUP BY p.name, e.olympic_id
        ORDER BY p.name
    )
SELECT name, olympic_id FROM PlayerMedals
WHERE gold > 0 AND silver > 0 AND bronze > 0;
