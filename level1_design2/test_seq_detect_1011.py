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
    
    for i in range(100):    
        # reset
        dut.reset.value = 1
        dut.inp_bit.value=0
        dut.seq_seen.value=0
        await FallingEdge(dut.clk)  
        dut.reset.value = 0

        N=7
        iparr=list()
        for i in range(0,N):
            await FallingEdge(dut.clk)
            iparr.append(random.randint(0,1))
            dut.inp_bit.value=iparr[i]
        print(iparr)
        
        if (iparr[0]==0):
            state='0'
        else:
            state='1'
        
        if (state=='0'):
            if(iparr[1]==0):
                state='0'
            else:
                state='1'
        elif (state=='1'):
            if(iparr[1]==0):
                state='10'
            else:
                state='1'

        if (state=='0'):
            if (iparr[2]==0):
                state='0'
            else:
                state='1'
        elif (state=='1'):
            if (iparr[2]==0):
                state='10'
            else:
                state='1'
        elif (state=='10'):
            if (iparr[2]==0):
                state='0'
            else:
                state='101'
        
        if (state=='0'):
            if (iparr[3]==0):
                state='0'
            else:
                state='1'
        elif (state=='1'):
            if (iparr[3]==0):
                state='10'
            else:
                state='1'
        elif (state=='10'):
            if (iparr[3]==0):
                state='0'
            else:
                state='101'
        elif (state=='101'):
            if (iparr[3]==0):
                state='0'
            else:
                state='1011'

        if (state=='0'):
            if (iparr[4]==0):
                state='0'
            else:
                state='1'
        elif (state=='1'):
            if (iparr[4]==0):
                state='10'
            else:
                state='1'
        elif (state=='10'):
            if (iparr[4]==0):
                state='0'
            else:
                state='101'
        elif (state=='101'):
            if (iparr[4]==0):
                state='0'
            else:
                state='1011'
        elif (state=='1011'):
            if (iparr[4]==0): #for 1011011- op1
                state='10'
            else:
                state='1'
        
        if (state=='0'):
            if (iparr[5]==0):
                state='0'
            else:
                state='1'
        elif (state=='1'):
            if (iparr[5]==0):
                state='10'
            else:
                state='1'
        elif (state=='10'):
            if (iparr[5]==0):
                state='0'
            else:
                state='101'
        elif (state=='101'):
            if (iparr[5]==0):
                state='0'
            else:
                state='1011'
        elif (state=='1011'):
            if (iparr[5]==0): #for 101101- op1
                state='10'
            else:
                state='1'
        
        if (state=='0'):
            if (iparr[6]==0):
                state='0'
            else:
                state='1'
        elif (state=='1'):
            if (iparr[6]==0):
                state='10'
            else:
                state='1'
        elif (state=='10'):
            if (iparr[6]==0):
                state='0'
            else:
                state='101'
        elif (state=='101'):
            if (iparr[6]==0):
                state='0'
            else:
                state='1011'
        elif (state=='1011'):
            if (iparr[6]==0): #for 101101- op1
                state='10'
            else:
                state='1'
        
        #check expop at each posedge clk

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