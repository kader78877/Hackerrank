select table_init.name
from 
(select friends.id, students.name, packages.salary
from friends
join students on friends.id = students.id
join packages on friends.id = packages.id
) table_init

left join
( select friends.id as id,friends.friend_id as friend_id,packages.salary as friend_salary
from friends
left join packages on packages.id = friends.friend_id
) table_friend
on table_friend.id=table_init.id

where table_init.salary < table_friend.friend_salary
order by table_friend.friend_salary
