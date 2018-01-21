import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class Test {
    public static void main(String[] args) {
        System.out.println("Good Day");
        int N = 10;
//        StdDraw.setXscale(0,1);
        StdDraw.setYscale(0,N);
//        StdDraw.setPenRadius(.01);
        for (int i = 0; i < N; i++){
//            StdDraw.point(i, i);
//            StdDraw.point(i, i*i);
//            StdDraw.point(i, i*Math.log(i));

            Double a_i = StdRandom.uniform(1.0, N);
            StdOut.println("---------");
            StdOut.println(a_i);
            StdOut.println(1.0*i/N);
            StdOut.println(a_i/2.0);
            StdOut.println(0.5/N);
            StdOut.println(a_i/2);
            StdDraw.filledRectangle(1.0*(i)/N+0.5/N, a_i/2.0, 0.5/N,a_i/2);
        }
        System.out.println(StdRandom.random());
    }
}
