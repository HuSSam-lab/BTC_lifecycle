IF -- Avoiding duplicating insert
	(SELECT TOP 1 cast([Date] as date)
	FROM [dbo].[Backup_real_time_prices]) >
	(SELECT TOP 1 cast([date] as date) 
	FROM [Raw] ORDER BY [date] desc)
		BEGIN -- getting the value from real time data base to row data base (whither it isn't found already)
			insert into [dbo].[Raw]
	        select * from [dbo].[Backup_real_time_prices]
		END;
ELSE--IF -- Avoiding duplicating insert
		BEGIN--	(SELECT TOP 1 cast([date] as date)
			SELECT * FROM  [Storing new historical prices] --	FROM [Storing new historical prices]) >
		END--	(SELECT TOP 1 cast([date] as date) 
--	FROM [Raw] ORDER BY [date] desc)
--		BEGIN -- getting the value from real time data base to row data base (whither it isn't found already)
--			insert into [Raw] ([Date], [BTC high], [ADA high], [BNB high], [ETH high], [SOL high], [XRP high])
--			select 
--			max([Date]) ,
--			sum([BTC high]) as [BTC high],
--			sum([ADA high]) as [ADA high],
--			sum([BNB high]) as [BNB high],
--			sum([ETH high]) as [ETH high],
--			sum([SOL high]) as [SOL high],
--			sum([XRP high]) as [XRP high]
--			from(
--			select
--				cast([date] as date) as [Date],
--			   CASE WHEN [Curr_name] = 'Bitcoin' THEN [Value] ELSE NULL END AS [BTC high],
--			   CASE WHEN [Curr_name] = 'Cardano' THEN [Value] ELSE NULL END AS [ADA high],
--			   CASE WHEN [Curr_name] = 'BNB' THEN [Value] ELSE NULL END AS [BNB high],
--			   CASE WHEN [Curr_name] = 'Ethereum' THEN [Value] ELSE NULL END AS [ETH high],
--			   CASE WHEN [Curr_name] = 'Solana' THEN [Value] ELSE NULL END AS [SOL high],
--			   CASE WHEN [Curr_name] = 'XRP' THEN [Value] ELSE NULL END AS [XRP high]
--					from [Storing new historical prices])
--				as combined_data
--		END;
--ELSE
--		BEGIN
--			SELECT * FROM  [Storing new historical prices] 
--		END