import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """
    listt1=[2749,2175,2429,2125,2178,2647,2816,2910,2299,2689]
    listt2=[0b0000,0b0001,0b0010,0b0011,0b0100,0b0101,0b0110,0b0111,0b1000,0b0001]
    
    #dut.accNumber.value=random.choice(listt1)
    dut.accNumber.value=2278
    #dut.pin.value=random.choice(listt2)
    dut.pin.value=0b0100
    dut.action=1
    
    if (dut.accNumber.value==2178 & dut.pin.value==0b0100):
        expop=1
    else: 
        expop=0
    print(dut.wasSuccessful.value)
    print(expop)
        
    assert dut.wasSuccessful.value==expop, "Randomised test failed. Expected output {B}, actual output {C}".format(B=expop, C=dut.wasSuccessful.value)
    #await 2 ns?