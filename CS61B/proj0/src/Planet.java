

public class Planet {
    double xxPos;
    double yyPos;
    double xxVel;
    double yyVel;
    double mass;
    String imgFileName;

    public Planet(double xP, double yP, double xV,
                  double yV, double m, String img){
        this.xxPos = xP;
        this.yyPos = yP;
        this.xxVel = xV;
        this.yyVel = yV;
        this.mass = m;
        this.imgFileName = img;
    }

    public Planet(Planet p){
        this.xxPos = p.xxPos;
        this.yyPos = p.yyPos;
        this.xxVel = p.xxVel;
        this.yyVel = p.yyVel;
        this.mass = p.mass;
        this.imgFileName = p.imgFileName;
    }
	
	public double calcDistance(Planet p){
		double x_square = Math.pow(this.xxPos - p.xxPos, 2);
		double y_square = Math.pow(this.yyPos - p.yyPos, 2);
		double r = Math.sqrt(x_square + y_square);
		return r;
	}

    public double calcForceExertedBy(Planet p){
        double G = 6.67e-11;
        double m1 = this.mass;
        double m2 = p.mass;
        double r = calcDistance(p);
        double r_square = Math.pow(r,2);
        return G * m1 * m2 / r_square;
    }

    public double calcForceExertedByX(Planet p){
        double r = calcDistance(p);
        double dx = p.xxPos - this.xxPos;
        if (r == 0){
            return 0.0;
        }else{
            return calcForceExertedBy(p) * dx / r;
        }
    }

    public double calcForceExertedByY(Planet p){
        double r = calcDistance(p);
        double dy = p.yyPos - this.yyPos ;
        if (r == 0){
            return 0.0;
        }else{
            return calcForceExertedBy(p) * dy / r;
        }
    }

    public double calcNetForceExertedByX(Planet[] allPlanets){
        double netForceExpertdByX = 0;
        for (Planet p : allPlanets){
            netForceExpertdByX += calcForceExertedByX(p);
        }
        return netForceExpertdByX;
    }

    public double calcNetForceExertedByY(Planet[] allPlanets){
        double netForceExpertdByY = 0;
        for (Planet p : allPlanets){
            netForceExpertdByY += calcForceExertedByY(p);
            //System.out.println(calcForceExertedByY(p));
        }
        return netForceExpertdByY;
    }

    public void update(double dt, double fX, double fY){
        double ax = fX / this.mass;
        double ay = fY / this.mass;
        this.xxVel += dt * ax;
        this.yyVel += dt * ay;
        this.xxPos += dt * this.xxVel;
        this.yyPos += dt * this.yyVel;
    }

    public void draw() {

        StdDraw.picture(this.xxPos, this.yyPos, "images/" + this.imgFileName);
//        StdDraw.show(2000);
    }

}
