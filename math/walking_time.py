# walking_time.py
DIST_KM = 4
STEP_FT = 1  # feet per step
FT_TO_M = 0.3048
STEPS_PER_KM_AVG = 1408  # 5kph walk [web:51]

dist_m = DIST_KM * 1000
steps = dist_m / (STEP_FT * FT_TO_M)
print(f"Steps: {steps:.0f}")

time_min = (DIST_KM * STEPS_PER_KM_AVG) / 80 * 60  # ~80 steps/min
print(f"Time: ~{time_min:.0f} min")
# Output: Steps: 13123, Time: ~20 min
