module Volume(input wire clk, rst, B,
          output reg S1,S0);
          
    reg S1_dash, S0_dash;

    always @(B,S1,S0)
        begin
            S1_dash = (~B &  S1 & ~S0) |  (~B &  S1 &  S0) | (B & ~S1 &  S0) | (B &  S1 & ~S0); 
            S0_dash = (~B & ~S1 &  S0) | (~B &  S1 &  S0) | (B & ~S1 & ~S0) |(B &  S1 & ~S0) ;
        end

    always @(posedge clk)
        begin
            if(rst)
                begin
                    S1 <= 0;
                    S0 <= 0;
                end
            else
                begin
                    S1 <= S1_dash;
                    S0 <= S0_dash;
                end
        end
endmodule
