module FullAdder(input wire A, B, Previous_Carry,
                output wire Sum, Carry);
    wire Sum_Case1, Sum_Case2, Sum_Case3, Sum_Case4;
    assign Sum_Case1 = ~A & ~B &  Previous_Carry;
    assign Sum_Case2 = ~A &  B & ~Previous_Carry;
    assign Sum_Case3 =  A & ~B & ~Previous_Carry;
    assign Sum_Case4 =  A &  B &  Previous_Carry;
    assign Sum = Sum_Case1 | Sum_Case2 | Sum_Case3 | Sum_Case4;

    wire Carry_Case1, Carry_Case2, Carry_Case3, Carry_Case4;
    assign Carry_Case1 = ~A &  B &  Previous_Carry;
    assign Carry_Case2 =  A & ~B &  Previous_Carry;
    assign Carry_Case3 =  A &  B & ~Previous_Carry;
    assign Carry_Case4 =  A &  B &  Previous_Carry;
    assign Carry = Carry_Case1 | Carry_Case2 | Carry_Case3 | Carry_Case4;
endmodule

module PAdder(input wire A, B,
             output wire Result);
    reg C_dash,C;
    HalfAdder HA0 (A[0], B[0],           Result[0], Carry[0]);
    FullAdder FA1 (A[1], B[1], Carry[0], Result[1], Carry[1]);
    FullAdder FA2 (A[2], B[2], Carry[1], Result[2], Result[3]);
endmodule
