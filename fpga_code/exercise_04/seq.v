module ex4(input wire clk, rst, B,
          output reg S1,S0);
    reg S1_dash, S0_dash;

    assign S1_dash = ~B &  S1 & ~S0 |
                     ~B &  S1 &  S0 |
                      B & ~S1 &  S0 |
                      B &  S1 & ~S0 ; 
    assign S0_dash = ~B & ~S1 &  S0 |
                     ~B &  S1 &  S0 |
                      B & ~S1 & ~S0 |
                      B &  S1 & ~S0 ;

    always @(poesedge clk)
        begin
            if(!rst)
                S1 <= 0;
                S0 <= 0;
            else
                S1 <= S1_dash;
                S0 <= S0_dash;
        end
endmodule
