from astropy.cosmology import WMAP9 as cosmo
from astropy import units as u

# ref :https://www.youtube.com/watch?v=2ZJEdce_4Zo
print()
print("enter input in format ScaleFactor CurrentDistance(in million Light Years) Obsarvable_Distance(in million Light Years)")
ScaleFactor, distance, observebableDistance = map(float, input().split())
redShift = lambda R : R-1
distance *= pow(10,6) * 3.06601e-7
observebableDistance *= pow(10,6) * 3.06601e-7
Hubblesconsst = cosmo.H(redShift(ScaleFactor))
velocity = Hubblesconsst*distance
time = (observebableDistance - distance) / velocity 
print(f"Remaining time for observations is : {time}")