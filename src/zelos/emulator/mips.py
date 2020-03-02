# Copyright (C) 2020 Zeropoint Dynamics

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/>.
# ======================================================================
import unicorn.mips_const as uc

from .base import IEmuHelper


class MipsEmuHelper(IEmuHelper):
    ip_reg = "pc"
    sp_reg = "sp"
    fp_reg = "fp"
    regmap = {
        "pc": uc.UC_MIPS_REG_PC,
        "0": uc.UC_MIPS_REG_0,
        "1": uc.UC_MIPS_REG_1,
        "2": uc.UC_MIPS_REG_2,
        "3": uc.UC_MIPS_REG_3,
        "4": uc.UC_MIPS_REG_4,
        "5": uc.UC_MIPS_REG_5,
        "6": uc.UC_MIPS_REG_6,
        "7": uc.UC_MIPS_REG_7,
        "8": uc.UC_MIPS_REG_8,
        "9": uc.UC_MIPS_REG_9,
        "10": uc.UC_MIPS_REG_10,
        "11": uc.UC_MIPS_REG_11,
        "12": uc.UC_MIPS_REG_12,
        "13": uc.UC_MIPS_REG_13,
        "14": uc.UC_MIPS_REG_14,
        "15": uc.UC_MIPS_REG_15,
        "16": uc.UC_MIPS_REG_16,
        "17": uc.UC_MIPS_REG_17,
        "18": uc.UC_MIPS_REG_18,
        "19": uc.UC_MIPS_REG_19,
        "20": uc.UC_MIPS_REG_20,
        "21": uc.UC_MIPS_REG_21,
        "22": uc.UC_MIPS_REG_22,
        "23": uc.UC_MIPS_REG_23,
        "24": uc.UC_MIPS_REG_24,
        "25": uc.UC_MIPS_REG_25,
        "26": uc.UC_MIPS_REG_26,
        "27": uc.UC_MIPS_REG_27,
        "28": uc.UC_MIPS_REG_28,
        "29": uc.UC_MIPS_REG_29,
        "30": uc.UC_MIPS_REG_30,
        "31": uc.UC_MIPS_REG_31,
        # DSP registers
        "dspccond": uc.UC_MIPS_REG_DSPCCOND,
        "dspcarry": uc.UC_MIPS_REG_DSPCARRY,
        "dspefi": uc.UC_MIPS_REG_DSPEFI,
        "dspoutflag": uc.UC_MIPS_REG_DSPOUTFLAG,
        "dspoutflag16_19": uc.UC_MIPS_REG_DSPOUTFLAG16_19,
        "dspoutflag20": uc.UC_MIPS_REG_DSPOUTFLAG20,
        "dspoutflag21": uc.UC_MIPS_REG_DSPOUTFLAG21,
        "dspoutflag22": uc.UC_MIPS_REG_DSPOUTFLAG22,
        "dspoutflag23": uc.UC_MIPS_REG_DSPOUTFLAG23,
        "dsppos": uc.UC_MIPS_REG_DSPPOS,
        "dspscount": uc.UC_MIPS_REG_DSPSCOUNT,
        # ACC registers
        "ac0": uc.UC_MIPS_REG_AC0,
        "ac1": uc.UC_MIPS_REG_AC1,
        "ac2": uc.UC_MIPS_REG_AC2,
        "ac3": uc.UC_MIPS_REG_AC3,
        # COP registers
        "cc0": uc.UC_MIPS_REG_CC0,
        "cc1": uc.UC_MIPS_REG_CC1,
        "cc2": uc.UC_MIPS_REG_CC2,
        "cc3": uc.UC_MIPS_REG_CC3,
        "cc4": uc.UC_MIPS_REG_CC4,
        "cc5": uc.UC_MIPS_REG_CC5,
        "cc6": uc.UC_MIPS_REG_CC6,
        "cc7": uc.UC_MIPS_REG_CC7,
        # FPU registers
        "f0": uc.UC_MIPS_REG_F0,
        "f1": uc.UC_MIPS_REG_F1,
        "f2": uc.UC_MIPS_REG_F2,
        "f3": uc.UC_MIPS_REG_F3,
        "f4": uc.UC_MIPS_REG_F4,
        "f5": uc.UC_MIPS_REG_F5,
        "f6": uc.UC_MIPS_REG_F6,
        "f7": uc.UC_MIPS_REG_F7,
        "f8": uc.UC_MIPS_REG_F8,
        "f9": uc.UC_MIPS_REG_F9,
        "f10": uc.UC_MIPS_REG_F10,
        "f11": uc.UC_MIPS_REG_F11,
        "f12": uc.UC_MIPS_REG_F12,
        "f13": uc.UC_MIPS_REG_F13,
        "f14": uc.UC_MIPS_REG_F14,
        "f15": uc.UC_MIPS_REG_F15,
        "f16": uc.UC_MIPS_REG_F16,
        "f17": uc.UC_MIPS_REG_F17,
        "f18": uc.UC_MIPS_REG_F18,
        "f19": uc.UC_MIPS_REG_F19,
        "f20": uc.UC_MIPS_REG_F20,
        "f21": uc.UC_MIPS_REG_F21,
        "f22": uc.UC_MIPS_REG_F22,
        "f23": uc.UC_MIPS_REG_F23,
        "f24": uc.UC_MIPS_REG_F24,
        "f25": uc.UC_MIPS_REG_F25,
        "f26": uc.UC_MIPS_REG_F26,
        "f27": uc.UC_MIPS_REG_F27,
        "f28": uc.UC_MIPS_REG_F28,
        "f29": uc.UC_MIPS_REG_F29,
        "f30": uc.UC_MIPS_REG_F30,
        "f31": uc.UC_MIPS_REG_F31,
        "fcc0": uc.UC_MIPS_REG_FCC0,
        "fcc1": uc.UC_MIPS_REG_FCC1,
        "fcc2": uc.UC_MIPS_REG_FCC2,
        "fcc3": uc.UC_MIPS_REG_FCC3,
        "fcc4": uc.UC_MIPS_REG_FCC4,
        "fcc5": uc.UC_MIPS_REG_FCC5,
        "fcc6": uc.UC_MIPS_REG_FCC6,
        "fcc7": uc.UC_MIPS_REG_FCC7,
        # AFPR128
        "w0": uc.UC_MIPS_REG_W0,
        "w1": uc.UC_MIPS_REG_W1,
        "w2": uc.UC_MIPS_REG_W2,
        "w3": uc.UC_MIPS_REG_W3,
        "w4": uc.UC_MIPS_REG_W4,
        "w5": uc.UC_MIPS_REG_W5,
        "w6": uc.UC_MIPS_REG_W6,
        "w7": uc.UC_MIPS_REG_W7,
        "w8": uc.UC_MIPS_REG_W8,
        "w9": uc.UC_MIPS_REG_W9,
        "w10": uc.UC_MIPS_REG_W10,
        "w11": uc.UC_MIPS_REG_W11,
        "w12": uc.UC_MIPS_REG_W12,
        "w13": uc.UC_MIPS_REG_W13,
        "w14": uc.UC_MIPS_REG_W14,
        "w15": uc.UC_MIPS_REG_W15,
        "w16": uc.UC_MIPS_REG_W16,
        "w17": uc.UC_MIPS_REG_W17,
        "w18": uc.UC_MIPS_REG_W18,
        "w19": uc.UC_MIPS_REG_W19,
        "w20": uc.UC_MIPS_REG_W20,
        "w21": uc.UC_MIPS_REG_W21,
        "w22": uc.UC_MIPS_REG_W22,
        "w23": uc.UC_MIPS_REG_W23,
        "w24": uc.UC_MIPS_REG_W24,
        "w25": uc.UC_MIPS_REG_W25,
        "w26": uc.UC_MIPS_REG_W26,
        "w27": uc.UC_MIPS_REG_W27,
        "w28": uc.UC_MIPS_REG_W28,
        "w29": uc.UC_MIPS_REG_W29,
        "w30": uc.UC_MIPS_REG_W30,
        "w31": uc.UC_MIPS_REG_W31,
        "hi": uc.UC_MIPS_REG_HI,
        "lo": uc.UC_MIPS_REG_LO,
        "p0": uc.UC_MIPS_REG_P0,
        "p1": uc.UC_MIPS_REG_P1,
        "p2": uc.UC_MIPS_REG_P2,
        "mpl0": uc.UC_MIPS_REG_MPL0,
        "mpl1": uc.UC_MIPS_REG_MPL1,
        "mpl2": uc.UC_MIPS_REG_MPL2,
        "ending": uc.UC_MIPS_REG_ENDING,
        "zero": uc.UC_MIPS_REG_ZERO,
        "at": uc.UC_MIPS_REG_AT,
        "v0": uc.UC_MIPS_REG_V0,
        "v1": uc.UC_MIPS_REG_V1,
        "a0": uc.UC_MIPS_REG_A0,
        "a1": uc.UC_MIPS_REG_A1,
        "a2": uc.UC_MIPS_REG_A2,
        "a3": uc.UC_MIPS_REG_A3,
        "t0": uc.UC_MIPS_REG_T0,
        "t1": uc.UC_MIPS_REG_T1,
        "t2": uc.UC_MIPS_REG_T2,
        "t3": uc.UC_MIPS_REG_T3,
        "t4": uc.UC_MIPS_REG_T4,
        "t5": uc.UC_MIPS_REG_T5,
        "t6": uc.UC_MIPS_REG_T6,
        "t7": uc.UC_MIPS_REG_T7,
        "s0": uc.UC_MIPS_REG_S0,
        "s1": uc.UC_MIPS_REG_S1,
        "s2": uc.UC_MIPS_REG_S2,
        "s3": uc.UC_MIPS_REG_S3,
        "s4": uc.UC_MIPS_REG_S4,
        "s5": uc.UC_MIPS_REG_S5,
        "s6": uc.UC_MIPS_REG_S6,
        "s7": uc.UC_MIPS_REG_S7,
        "t8": uc.UC_MIPS_REG_T8,
        "t9": uc.UC_MIPS_REG_T9,
        "k0": uc.UC_MIPS_REG_K0,
        "k1": uc.UC_MIPS_REG_K1,
        "gp": uc.UC_MIPS_REG_GP,
        "sp": uc.UC_MIPS_REG_SP,
        "fp": uc.UC_MIPS_REG_FP,
        "s8": uc.UC_MIPS_REG_S8,
        "ra": uc.UC_MIPS_REG_RA,
        "hi0": uc.UC_MIPS_REG_HI0,
        "hi1": uc.UC_MIPS_REG_HI1,
        "hi2": uc.UC_MIPS_REG_HI2,
        "hi3": uc.UC_MIPS_REG_HI3,
        "lo0": uc.UC_MIPS_REG_LO0,
        "lo1": uc.UC_MIPS_REG_LO1,
        "lo2": uc.UC_MIPS_REG_LO2,
        "lo3": uc.UC_MIPS_REG_LO3,
        "cp0_userlocal": uc.UC_MIPS_REG_CP0_USERLOCAL,
    }

    imp_regs = [
        "zero",
        "at",
        "v0",
        "v1",
        "a0",
        "a1",
        "a2",
        "a3",
        "t0",
        "t1",
        "t2",
        "t3",
        "t4",
        "t5",
        "t6",
        "t7",
        "s0",
        "s1",
        "s2",
        "s3",
        "s4",
        "s5",
        "s6",
        "s7",
        "t8",
        "t9",
        "k0",
        "k1",
        "gp",
        "sp",
        "s8",
        "ra",
        "lo",
        "hi",
        "pc",
    ]
    # 'sr', #missing
    # 'bad', #missing
    # 'cause', #missing