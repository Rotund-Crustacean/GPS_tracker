import banana
import NMEA
b = banana.Banana('cat')
d = banana.Banana('dog')



print(b.five_characters('rkghwacui'))

print(d.five_characters('rkghwacui'))

print(b.more_five_characters('rkghwacui'))

print(d.more_five_characters('rkghwacui'))


nema = NMEA.NMEA()

print(nema.decode_line('csiuhgiosiru'))
