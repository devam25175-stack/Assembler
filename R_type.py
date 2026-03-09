reg_map = {
"zero":0,"ra":1,"sp":2,"gp":3,"tp":4,
"t0":5,"t1":6,"t2":7,
"s0":8,"s1":9,
"a0":10,"a1":11,"a2":12,"a3":13,"a4":14,"a5":15,"a6":16,"a7":17,
"s2":18,"s3":19,"s4":20,"s5":21,"s6":22,"s7":23,"s8":24,"s9":25,"s10":26,"s11":27,
"t3":28,"t4":29,"t5":30,"t6":31
}

def r_type(unit, idx):

    # funct7 values
    funct7_map = {"add":"0000000","sub":"0100000","sll":"0000000","slt":"0000000",
                  "sltu":"0000000","xor":"0000000","srl":"0000000","or":"0000000","and":"0000000"}

    # funct3 values
    funct3_map = {"add":"000","sub":"000","sll":"001","slt":"010",
                  "sltu":"011","xor":"100","srl":"101","or":"110","and":"111"}

    opcode = "0110011"   # opcode for r type instructions

    # r type instruction should have 4 parts
    if len(unit) != 4:
        raise ValueError("Line " + str(idx) + ": invalid r type instruction")

    op = unit[0]
    rd = unit[1]
    rs1 = unit[2]
    rs2 = unit[3]

    # checking registers
    if rd not in reg_map:
        raise ValueError("Line " + str(idx) + ": invalid register")

    if rs1 not in reg_map:
        raise ValueError("Line " + str(idx) + ": invalid register")

    if rs2 not in reg_map:
        raise ValueError("Line " + str(idx) + ": invalid register")

    # convert registers to binary
    rd_bin = format(reg_map[rd], "05b")
    rs1_bin = format(reg_map[rs1], "05b")
    rs2_bin = format(reg_map[rs2], "05b")

    funct7 = funct7_map[op]
    funct3 = funct3_map[op]

    # combine everything
    final_inst = funct7 + rs2_bin + rs1_bin + funct3 + rd_bin + opcode

    return final_inst

