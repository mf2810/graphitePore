import sys

####################### DEFINING SPACES ###########################
sig = float(sys.argv[1])
yD  = float(sys.argv[2])

####################### INITIALISATION ############################
x0, y0, z0 = 0, 0, 0 
x, y, z = 0, 0, 0


####################### DEFINING BOX SIZES ########################

#box = [4.,4.,6.]
box = [float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])]

reps = [int(box[0]/1.5/sig), int(box[1]/yD), int(box[2]/(((3**.5)/2.)*sig))]
#reps = [10,10,10]
#print reps
#exit()
cntr = 0
totz = reps[0]*reps[1]*reps[2]
xF, yF, zF = round(reps[0]*1.5,0)*sig, yD* reps[1], ((3**.5)/2.) * sig * reps[2]

print("generating graphite")
print("%i" % totz )

for k in range(0,reps[1]):
    if k % 2 != 0:
        x0 = x0 + sig
        #y0 = y0 + ((3**.5)/2.)*sig
        y0 = y0
    else:
        x0 = 0
        y0 = 0

    if k == 0:
        z  = 0
    else:
        z = z + yD

    for j in range(0,reps[2]):
        if (j % 2) != 0:
            x = x0
        else:
            x = x0 + sig/2.

        if j == 0:
            y=y0
        else:
            y = y+((3**.5)/2.)*sig

        for i in range(0,reps[0]):
            cntr = cntr + 1 
            print ("%5d%-5s%5s%5d%8.3f%8.3f%8.3f%8.4f%8.4f%8.4f" %(cntr, 'GAE', 'GA', cntr, x, z, y, 0, 0, 0))
            if (j % 2) != 0:
                if (i % 2) != 0:
                    x=x + sig
                else:
                    x = x + 2* sig
            else:
                if (i % 2) != 0:
                    x=x + 2* sig
                else:
                    x = x + sig

print ("%10.5f%10.5f%10.5f" %(xF, yF, zF))
