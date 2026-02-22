package Inheritance;

class multi {
	int a,b;
	double c,d;
	multi(int x, int y){
		a = x;
		b = y;
	}
	multi(double u, double v){
		c = u;
		d = v;
	}
}

public class q3 {

	public static void main(String[] args) {
		multi o = new multi(2,5);
		multi o1 = new multi(2.34,3.455);
		System.out.println(o.a*o.b);
		System.out.println(o1.c*o1.d);
	}
	
//	

}
