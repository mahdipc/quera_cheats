import java.util.Scanner;

public class Q139970 {
  public static void main(String... args) {
    Scanner scn = new Scanner(System.in);
    long n = scn.nextInt();
    System.out.print((n * n - n) / 2 + n);
  }

}