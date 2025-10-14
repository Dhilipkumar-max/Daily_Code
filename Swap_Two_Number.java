public class Main{
  public static void main(String[] args){
    int a = 5;
    int b = 10;
    System.out.println("a = "+a);
    System.out.println("b = "+b);
    int temb = a;
    a = b;
    b = temb;
    System.out.println("a = "+a);
    System.out.println("b = "+b);
  }
}
    
