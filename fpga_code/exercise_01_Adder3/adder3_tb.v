`timescale 1ns / 1ps

module TB;
   
   reg  [2:0] A, B;
   wire [3:0] ANS;

   Adder3 adder_3b(A, B, ANS);

   initial begin
      $monitor ($time, ": Adder3: A: %x, B: %x, ANS: %x", A, B, ANS);
      #1;
      A = 0;
      B = 0;
      #5;
      A = 3'h1;
      B = 3'h0;
      #1;
      A = 3'h1;
      B = 3'h1;
      #1;
      A = 3'h2;
      B = 3'h1;
      #1;
      A = 3'h2;
      B = 3'h2;
      #1;
      A = 3'h3;
      B = 3'h2;
      #1;
      A = 3'h3;
      B = 3'h3;
      #1;
      A = 3'h4;
      B = 3'h3;
      #1;
      A = 3'h4;
      B = 3'h4;
      #1;
      A = 3'h5;
      B = 3'h4;
      #1;
      A = 3'h5;
      B = 3'h5;
      #1;
      A = 3'h6;
      B = 3'h5;
      #1;
      A = 3'h6;
      B = 3'h6;
      #1;
      A = 3'h7;
      B = 3'h6;
      #1;
      A = 3'h7;
      B = 3'h7;
      
      # 5;


   end

endmodule
