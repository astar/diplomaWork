-- get objects star,galaxy,qso objects from SDSS database

select top 100 u-g,g-r,r-i,s.specClass
from PhotoPrimary p join SpecPhotoAll s on p.objid=s.objid 
where s.specClass in (1)
and u between 18 and 19
and u is not null
and g is not null
and r is not null
and i is not null
union all
select top 100 u-g,g-r,r-i,s.specClass
from PhotoPrimary p join SpecPhotoAll s on p.objid=s.objid 
where s.specClass in (2)
and u between 18 and 19
and u is not null
and g is not null
and r is not null
and i is not null
union all
select top 100 u-g,g-r,r-i,s.specClass
from PhotoPrimary p join SpecPhotoAll s on p.objid=s.objid 
where s.specClass in (3)
and u between 18 and 19
and u is not null
and g is not null
and r is not null
and i is not null
