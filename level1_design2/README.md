<img width="959" alt="Screenshot 2022-08-01 at 23 27 19" src="https://user-images.githubusercontent.com/61197146/182212010-f182ea88-aaf1-4b71-ab79-1d87f22ec3aa.png">

Input cases-
At each falling edge of the clock for N cycles, a random bit is given as input and all the N inputs are stored in an array for inp_bit sequence.

N=7
iparr=list()
for i in range(0,N):
     await FallingEdge(dut.clk)
     iparr.append(random.randint(0,1))
     dut.inp_bit.value=iparr[i]
     print(iparr)
     
Error-
assert dut.seq_seen.value==expop, "Randomised test failed. Expected output {B}, actual output {C}".format(B=expop, C=dut.seq_seen.value)

AssertionError: Randomised test failed. Expected output 1, actual output 0

inp_bit sequence is given as [0, 0, 1, 1, 0, 1, 1]
Expected output is 1 as the sequence detector is overlapping
Actual output is 0 from DUT

Bugs-

The bug shows that there is an error in overlap detection. In can be resolved in SEQ_1 and SEQ_1011 cases as shown in seq_detect_1011_corrected.v
