#!/bin/bash

# ALL LENGTHS IN NM

# PORE INFORMATION
ccD=0.14 # carbon carbon bond length 
yD=0.34  # interlater distance of graphite
inputDx=3.0 #length of graphite in x
inputDy=3.0 #length of graphite in x
inputDz=12.0 #length of graphite in x

# BOX INFORMATION
poreWidth=3.0
zL=60

python graphiteGen.py $ccD $yD $inputDx $inputDy $inputDz > datafile.gro

rm pore.gro


x=$(tail -1 datafile.gro | awk '{print $1}')
y=$(tail -1 datafile.gro | awk '{print $(NF-1)}')
z=$(tail -1 datafile.gro | awk '{print $(NF)}')

poreWidth=$(python -c "print ${poreWidth}+${y}")

editconf -f datafile.gro -o pore.gro -box ${x} ${poreWidth} ${zL}
#editconf -f datafile.gro -o pore.gro -box ${x} ${poreWidth} ${z}

y2=$(tail -1 pore.gro | awk '{print $(NF-1)}')
b=$(python -c "print ${y2}*.50")

editconf -f pore.gro -o pore.gro -translate 0 ${b} 0 

rm datafile.gro \#*
rm  \#*
echo ${z}
