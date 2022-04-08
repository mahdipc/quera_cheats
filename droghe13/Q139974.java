import java.util.Scanner;

public class Q139974 {
    static char[] vowels = { 'a', 'e', 'i', 'o', 'u' };

    public static void main(String... args) {
        Scanner scn = new Scanner(System.in);
        String s = scn.nextLine();
        int v = count(s);
        System.out.print(v);
    }

    private static int count(String s) {
        int v = 0;
        char[] chars = s.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            if (contains(chars[i]))
                v++;
        }
        return v;
    }

    private static boolean contains(char c) {
        for (int i = 0; i < vowels.length; i++) {
            if (c == vowels[i])
                return true;
        }
        return false;
    }
}