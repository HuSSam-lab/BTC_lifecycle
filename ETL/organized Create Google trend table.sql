DECLARE @start Date = (select top(1) [date] from [dbo].[Google Trend Staging DB] )
DECLARE @end Date =( select top(1) [date] from [dbo].[Google Trend Staging DB] order by [date] desc)
DECLARE @currentDate Date = @start
DECLARE @nextDate Date = @start
DECLARE @FOmonth Date = @start

WHILE @nextDate <= @end -- month of year loop
BEGIN
	SET @nextDate =  DATEADD(MONTH, 1, @nextDate)
	WHILE @currentDate < @nextDate --- days loop
		BEGIN
			insert into [extended_google_trend] 
			select @currentDate,[worldwide], [unitedstates],[Germany], [UAE], [Dubai]
			from [Google Trend Staging DB]
			where [date] = DATEADD(MONTH, -1, @nextDate)
			SET @currentDate = DATEADD(day, 1, @currentDate);
		END
		SET @FOmonth = @nextDate
END;



--create table extended_google_trend (
--[date] date not null,
--[worldwide] real,
--[unitedstates] real,
--[Germany] real,
--[UAE] real,
--[Dubai] real)
