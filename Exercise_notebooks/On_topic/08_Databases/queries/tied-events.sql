-- Report all `individual events' where there was a tie in the score, and two or
-- more players got awarded a Gold medal. The 'Events' table contains information
-- about whether an event is individual or not. 

SELECT r.event_id, count(r.medal) as medals
FROM Results r
    JOIN Events e ON e.event_id = r.event_id
WHERE e.is_team_event = 0 AND r.medal = 'GOLD'
GROUP BY r.event_id
HAVING count(r.medal) > 1;
