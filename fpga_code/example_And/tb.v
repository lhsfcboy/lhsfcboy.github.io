`timescale 1ns / 1ps

module TB;
   
   reg  A, B;
   wire Y;

   And and_1b(A, B, Y);

   initial begin
      $monitor ($time, ": And: A: %x, B: %x, ANS: %x", A, B, Y);
      #1;
      A = 1'b0;
      B = 1'b0;
      #5;
      A = 1'b0;
      B = 1'b1;
      #1;
      A = 1'b1;
      B = 1'b0;
      #1;
      A = 1'b1;
      B = 1'b1;
      
      # 5;
   end

endmodule
