# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    ip=random.randint(0,1)
    ip1=random.randint(0,1)
    ip2=random.randint(0,1)
    ip3=random.randint(0,1)

    await FallingEdge(dut.clk)
    dut.inp_bit.value=ip
    if (ip==1)
        STATE1=1
    else STATE1=0
    await FallingEdge(dut.clk)
    dut.inp_bit.value=ip1
    if (STATE1==1)
        if (ip1==1)
            STATE10=0
        else STATE10=1
    else 
        if (ip1==1)
            STATE1=1
        else STATE1=0
    await FallingEdge(dut.clk)
    dut.inp_bit.value=ip2
    if (STATE10==1)
        if (ip2==1)
            STATE101=1
        else STATE1=0
    else 
        if (ip1==1)
            STATE1=1
        else STATE1=0


    

    assert dut.seq_seen.value==expout, "Randomised test failed, for input {A}. Expected output {B}, actual output {C}".format(A=SEL, B=expout, C=dut.seq_seen.value)
#await 2 ns?