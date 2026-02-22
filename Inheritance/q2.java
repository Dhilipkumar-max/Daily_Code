package Inheritance;

public class q2 
{
	
	public static void main(String[] args) 
	{
		rit o = new rit();
		o.disp();
		rit o1 = new rec();
		o1.disp();
		
	}	
}
	
class rit{
		public void disp() {
			System.out.println("RIT");
		}
	}
class rec extends rit{
		public void disp() {
			System.out.println("REC");
		}
	}
