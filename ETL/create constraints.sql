-- --don't forget to set the google date to primary key and raw date to not null
	--ALTER TABLE  [dbo].[extended_google_trend] 
	--ADD constraint google_fk FOREIGN KEY ([date])
	--REFERENCES [Raw] ([Date]) on delete cascade  
	
	--ALTER TABLE [Twitter_analyzied]
	--ADD constraint twitter_analyzied_fk FOREIGN KEY  ([date])
	--REFERENCES [Raw] ([Date]) on delete cascade  
DECLARE @constraints int = 0

SET @constraints = (SELECT count(*) FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE (TABLE_NAME = 'Raw' AND COLUMN_NAME = 'Date'))

SET @constraints = @constraints + (SELECT count(*) FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE (TABLE_NAME = 'Twitter_analyzied' AND COLUMN_NAME = 'date'))


if @constraints = 1
	begin
	ALTER TABLE [Raw]
	ADD constraint google_fk FOREIGN KEY  ([Date])
	REFERENCES  [extended_google_trend]  ([date])

	ALTER TABLE [Twitter_analyzied]
	ADD constraint twitter_analyzied_fk FOREIGN KEY  ([date])
	REFERENCES [Raw] ([date])
	end


