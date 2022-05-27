-- This query yields the number of shootings with at least one death

SELECT State, count(State) as [No. of shootings with at least one death]
FROM shootingdata
WHERE Killed > 0
GROUP by State
ORDER by count(State) DESC