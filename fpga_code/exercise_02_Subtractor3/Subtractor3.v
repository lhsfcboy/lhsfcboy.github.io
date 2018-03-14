module HalfAdder(input wire A, B,
                output wire Sum, Carry);
    assign Sum = (~A & B) | (A & ~B);
    assign Carry = A & B;
endmodule

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

module Adder3(input wire [2:0]A, [2:0]B,
             output wire [3:0]Result);
    wire [1:0]Carry;
    HalfAdder HA0 (A[0], B[0],           Result[0], Carry[0]);
    FullAdder FA1 (A[1], B[1], Carry[0], Result[1], Carry[1]);
    FullAdder FA2 (A[2], B[2], Carry[1], Result[2], Result[3]);
endmodule

module Complementer(input wire [2:0]B,
                   output wire [2:0]B_minus);
    wire [2:0]B_invert;
    assign B_invert[0] = ~B[0];
    assign B_invert[1] = ~B[1];
    assign B_invert[2] = ~B[2];
endmodule
