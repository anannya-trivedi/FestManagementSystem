use fest_management;



-- Query1
-- No. of tickets sold for a particular event, Music for instance
select soldNo from ticket3 where Ename="Music";




-- Query2
-- The event names for which the tickets have been sold out
select Ename from ticket3 where AvailableNo=0;




-- Query3
-- Total revenue generated from ticket sales of a particular festival event, Music for instance
select (SoldNo*Price) from ticket2 natural join ticket3 where Ename="Music";




-- Query4
-- Names of Vendors who have applied to participate in the festival
select VName from vendor3 group by VName;




-- Query5
-- The no. of attendees who have purchased tickets for a particular event, concert for instance
-- the number of attendees=the no. of tickets sold for that event
select soldNo from ticket3 where Ename="concert";




-- Query6
-- Names of sponsors for a particular event, Music for instance
select Logo_Name from sponsors where Ename="Music";




-- Query7
-- Event Name with the highest attendance
-- The event for which maximum tickets have been sold will be having the maximum no. of attendees
select Ename from ticket3 where soldNo=(select max(soldNo) from ticket3);




-- Query8
-- Average ticket price for a particular event, mime for instance
select avg(Price) from ticket2 where Ename="mime";





-- Query9
-- Performer Name of a particular event, mime for instance 
select Pname from performer where Ename="mime";




-- Query10
-- The sum total of the tickets sold for all the events 
select sum(soldNo) from ticket3;





-- Query 11
-- The name of events on a particular date, 5 dec 23 for instance
select EName from event where EDate='2023-12-05';











