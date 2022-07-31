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

    iparr=list()
    # reset
    dut.reset.value = 1
    dut.inp_bit.value=0
    dut.seq_seen.value=0
    await FallingEdge(dut.clk)  
    dut.reset.value = 0

    await FallingEdge(dut.clk)
    ip=random.randint(0,1)
    dut.inp_bit.value=ip
    iparr.append(ip)

    await FallingEdge(dut.clk)
    ip1=random.randint(0,1)
    dut.inp_bit.value=ip1
    iparr.append(ip1)

    await FallingEdge(dut.clk)
    ip2=random.randint(0,1)
    dut.inp_bit.value=ip2
    iparr.append(ip2)

    await FallingEdge(dut.clk)
    ip3=random.randint(0,1)
    dut.inp_bit.value=ip3
    iparr.append(ip3)

    print(iparr)

    
    
    if (iparr[0]==0):
        state='0'
    else:
        state='1'
    
    if (state=='1'):
        if(iparr[1]==0):
            state='10'
        else:
            state='1'
    else:
        if(iparr[1]==0):
            state='0'
        else:
            state='1'

    if (state=='1'):
        if (iparr[2]==0):
            state='10'
        elif (iparr[2]==1):
            state='1'
    elif (state=='0'):
        if (iparr[2]==0):
            state='0'
        elif (iparr[2]==1):
            state='1'
    elif (state=='10'):
        if (iparr[2]==0):
            state='0'
        elif (iparr[2]==1):
            state='101'
    
    if (state=='0'):
        if (iparr[3]==0):
            state='0'
        elif (iparr[3]==1):
            state='1'
    elif (state=='1'):
        if (iparr[3]==0):
            state='10'
        elif (iparr[3]==1):
            state='1'
    elif (state=='10'):
        if (iparr[3]==0):
            state='0'
        elif (iparr[3]==1):
            state='101'
    elif (state=='101'):
        if (iparr[3]==0):
            state='0'
        elif (iparr[3]==1):
            state='1011'

    await FallingEdge(dut.clk)
    await RisingEdge(dut.clk)
    if (state=='1011'):
        expop=1
    else:
        expop=0




    print(expop)
    print(dut.seq_seen.value)
    
    assert dut.seq_seen.value==expop, "Randomised test failed. Expected output {B}, actual output {C}".format(B=expop, C=dut.seq_seen.value)
#await 2 ns?