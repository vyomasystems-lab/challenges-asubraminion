
MUX Design Verification

<img width="1007" alt="Screenshot 2022-08-01 at 23 17 49" src="https://user-images.githubusercontent.com/61197146/182210607-16888cc6-ed1d-4f2c-a9eb-e0523f292f52.png">

First test for first half of the possible cases-
SEL=random.randint(0,15)
dut.sel.value=SEL

Second test for second half of the possible cases-
SEL=random.randint(16,30)
dut.sel.value=SEL

Test scenario-
Random test values are given

Error observed-
AssertionError: Randomised test failed, for SEL=13, output should be 1 (decimal), but is found to be 10 (binary)
AssertionError: Randomised test failed, for SEL=12, output should be 2 (decimal), but is found to be 00 (binary)

Corrected Verilog code is available in mux_corrected.v 




assert dut.out.value==inputt[SEL]
