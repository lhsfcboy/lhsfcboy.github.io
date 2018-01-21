public class NBody {

    public static double readRadius(String planetsTxtPath) {
        In in = new In(planetsTxtPath);
        int rank = in.readInt();
        return in.readDouble();
    }

    public static Planet[] readPlanets(String planetsTxtPath){
        In in = new In(planetsTxtPath);
        int planetNumbers = in.readInt();
        in.readDouble();
        Planet[] allPlanets = new Planet[planetNumbers];

        for ( int i =0; i < planetNumbers; i += 1){
            allPlanets[i] = new Planet(in.readDouble(), in.readDouble(),
                    in.readDouble(), in.readDouble(), in.readDouble(), in.readString());
        }

        return allPlanets;
    }

    public static void main(String[] args){
        double T = Double.parseDouble(args[0]);
        double dt = Double.parseDouble(args[1]);
        String filename = args[2];
        double radius = readRadius(filename);

        In in = new In(filename);
        int numOfPlanets = in.readInt();
        Planet[] allPlanets = readPlanets(filename);

        StdDraw.setScale(-radius, radius);

        for (int t = 0; t <= T; t += dt) {
            StdDraw.picture(0, 0, "images/starfield.jpg");
            for (Planet p : allPlanets) {
                p.update(dt,p.calcNetForceExertedByX(allPlanets),
                            p.calcNetForceExertedByY(allPlanets));
//                cur.setNetForce(planets);
//                cur.update(dt);
                p.draw();
            }
            StdDraw.show(10);
        }

    }

}
