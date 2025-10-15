public class Main{
  public static void main(String[] args){
    int num=1234;
    int digit=0;
    while (num!=0){
      int count= num%10;
      digit = digit*10+count;
      num/=10;
    System.out.println(digit);
    }
  }
