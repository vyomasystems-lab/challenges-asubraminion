# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    inputt=[0b01,0b00,0b11,0b10,0b01,0b00,0b10,0b00,0b11,0b10,0b00,0b01,0b10,0b01,0b11,0b01,0b10,0b00,0b10,0b11,0b11,0b01,0b00,0b10,0b01,0b10,0b11,0b11,0b10,0b01,0b00]
    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp0.value=inputt[0]
    dut.inp1.value=inputt[1]
    dut.inp2.value=inputt[2]
    dut.inp3.value=inputt[3]
    dut.inp4.value=inputt[4]
    dut.inp5.value=inputt[5]
    dut.inp6.value=inputt[6]
    dut.inp7.value=inputt[7]
    dut.inp8.value=inputt[8]
    dut.inp9.value=inputt[9]
    dut.inp10.value=inputt[10]
    dut.inp11.value=inputt[11]
    dut.inp12.value=inputt[12]
    dut.inp13.value=inputt[13]
    dut.inp14.value=inputt[14]
    dut.inp15.value=inputt[15]
    dut.inp16.value=inputt[16]
    dut.inp17.value=inputt[17]
    dut.inp18.value=inputt[18]
    dut.inp19.value=inputt[19]
    dut.inp20.value=inputt[20]
    dut.inp21.value=inputt[21]
    dut.inp22.value=inputt[22]
    dut.inp23.value=inputt[23]
    dut.inp24.value=inputt[24]
    dut.inp25.value=inputt[25]
    dut.inp26.value=inputt[26]
    dut.inp27.value=inputt[27]
    dut.inp28.value=inputt[28]
    dut.inp29.value=inputt[29]
    dut.inp30.value=inputt[30]

    for i in range(200):
        SEL=random.randint(0,30)
        dut.sel.value=SEL

        await Timer (2,units='ns')
        #print(inputt[SEL])
        #print(dut.out.value)
        assert dut.out.value==inputt[SEL], "Randomised test failed, for SEL={A}, output should be {B} (decimal), but is found to be {C} (binary)".format(A=SEL, B=inputt[SEL], C=dut.out.value)
