<img width="953" alt="Screenshot 2022-08-01 at 23 36 16" src="https://user-images.githubusercontent.com/61197146/182213373-f24ab8b5-9f0f-4b5b-b5a3-80c01f9af266.png">

Randomised inputs are given for 10 iterations to observe possible failures of the DUT.

Input failure combination-

dut.mav_putvalue_src1.value = 0xa
dut.mav_putvalue_src2.value = 0x9
dut.mav_putvalue_src3.value = 0x3
dut.mav_putvalue_instr.value = 0x101010b3
(Output enable is set as high) 

Error-
AssertionError: Value mismatch DUT = 0x14 does not match MODEL = 0x0
