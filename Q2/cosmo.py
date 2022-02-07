from astropy.cosmology import WMAP9 as cosmo

# ref :https://www.youtube.com/watch?v=2ZJEdce_4Zo
print("enter input in formagt ScaleFactor CurrentDistance Obsarvable_Distance")
ScaleFactor, distance, observebableDistance = map(float, input().split())
redShift = lambda R : R-1
Hubblesconsst = cosmo.H(redShift(ScaleFactor))
velocity = Hubblesconsst*distance
time = (observebableDistance - distance) / velocity 
print(f"Remaining time for observations is : {time}")

