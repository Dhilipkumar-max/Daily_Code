import java.util.*;
public class Main{
  public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
    int age =sc.nextInt();
    if(age<=18){
      System.out.println("Not Allow to vote");
    }else if (age>18){
      System.out.println("Allow to vote");
    }else {
      Sytem.out.println("Invalid input");
    }
  }
}
