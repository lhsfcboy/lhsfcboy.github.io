package Chapter01;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class Exercise1_1_11 {
    public static void main(String[] args) {
        int rowNum = 10;
        int columnNam = 10;
        Boolean[][] data = new Boolean[rowNum][columnNam];

        for(int i = 0; i < rowNum; i++){
            for(int j = 0; j < columnNam; j ++){
                data[i][j] = StdRandom.bernoulli();
//                StdOut(i, j, data[i][j]);
            }
//            System.out.println();
        }

        for(int i = 0; i < rowNum; i++){
            System.out.print(i);

            for(int j = 0; j < columnNam; j ++){
                String temp;
                if (data[i][j]){
                    temp = "*";
                }else{
                    temp = " ";
                }
                System.out.print(temp);
            }

            System.out.println();
        }
    }
}
