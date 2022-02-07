from astropy.cosmology import WMAP9 as cosmo
from astropy import units as u

print()
print("enter input in format ScaleFactor CurrentDistance(in million Light Years) Obsarvable_Distance(in million Light Years)")
ScaleFactor, distance, observebableDistance = map(float, input().split())
redShift = lambda R : R-1
distance *= pow(10,6)  *u.lyr
observebableDistance *= pow(10,6) * u.lyr
Hubblesconsst = cosmo.H(redShift(ScaleFactor)).to(u.kilometer/(u.kilometer*u.second))
velocity = Hubblesconsst*distance
time = ((observebableDistance - distance) / velocity ).to(u.year)
print(f"Remaining time for observations is : {time}")
print()
