import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
//输出所有数的平均值
public class Average {
 
    public static void main(String[] args) {
        int count = 0;
        double sum = 0.0;
        while (!StdIn.isEmpty()) {
            double value = StdIn.readDouble();
            sum += value;
            count++;
        }
        double average = sum / count;
        StdOut.printf("Average is %.5f\n", average);
    }
}
