--- this way i don't use it because i use data flow to get the twitter analyzied
create table [Twitter_analyzied](
[count] int,
[date] date primary key not null,
sum_user_verified int,
sum_is_retweet int,
sum_is_old_user int,
sum_user_important int)


insert into [Twitter_analyzied]
select count(*) as [count],[date] as [date], sum(user_verified) as sum_user_verified, sum(is_retweet) as sum_is_retweet, sum(Is_old_User) as sum_is_old_user, sum(user_important) as sum_user_important
from [Twitter staging DB]
group by [date]

drop table [dbo].[Twitter_analyzied]