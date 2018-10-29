import math

r = 5.4
h = 7.9

print("Har en sirkel med radius", r, "som er grunnflate i en sylinder med høyde", h)
omkrets = math.tau * r
print("Omkrets av sirkelen:", omkrets)  # tau er det samme som 2 pi
areal = math.pi * r ** 2
print("Areal av sirkelen:", round(areal))
print("Areal av sylinderen:", omkrets * h + 2 * areal)