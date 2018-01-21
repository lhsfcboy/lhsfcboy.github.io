package Chapter01;

public class IntToBinaryString {
    public static void main(String[] args) {
        String s = "";
        int N = 25;
        for (int n = N; n > 0; n /= 2 ){
            s = (n % 2) + s;
            System.out.println(n/2);
            System.out.println(s);
        }

    }
}
