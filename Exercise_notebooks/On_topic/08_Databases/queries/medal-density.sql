-- For 2000 Olympics, find the 5 countries with the largest values of
-- ``number-of-team-medals/area_sqkm''.

WITH TeamMedalCounts AS (
        SELECT m.country_id, COUNT(m.medal) as team_medals
        FROM TeamMedals m
            JOIN Events e ON e.event_id = m.event_id
        WHERE e.olympic_id = (SELECT olympic_id FROM Olympics WHERE year=2000)
        GROUP BY country_id
    ), TeamMedalDensity AS (
        SELECT tmc.country_id, tmc.team_medals::float/c.area_sqkm::float as team_medal_density
        FROM TeamMedalCounts tmc
            JOIN Countries c ON c.country_id = tmc.country_id
        ORDER BY team_medal_density DESC
    ), RankedCountries AS (
        SELECT row_number() over () as rownum, t.*
        FROM TeamMedalDensity t
    )
SELECT country_id, team_medal_density FROM RankedCountries
    WHERE rownum <= 5;
