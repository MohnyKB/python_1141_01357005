        add $s1, $s3, zero
loop1:
        slt $t0, zero, $s1
        beq $t0, zero, exit1

        add $s2, $s4, zero
loop2:
        slt $t1, zero, $s2
        beq $t1, zero, exit2

        add $t2, $s1, $s2 #t2 = s1 + s2
        sll $t3, t2, 2
        add $t4, $s5, $t3 #t4 = &s5[s1+s2]
        lw  $t5, 0($t4) #t5 = s5[s1+s2]
        add $t5, $t5, $t2 #t5 = t5 + s1 + s2
        sw $t5, 0($t4)

        addi $s2, $s2, -1
        j loop2
exit2:
        addi $s1, $s1, -1
        j loop1
exit1: