import java.net.InetAddress;


public class ShowLocalIP {
    public static void main(String[] args) {
        try {

            System.out.print(InetAddress.getLocalHost());
        } catch(Exception e){
            e.printStackTrace();
        }

    }

}
