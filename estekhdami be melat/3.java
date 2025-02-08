import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        
        // Read n and q using var for local type inference
        var firstLine = scanner.nextLine().split(" ");
        var n = Integer.parseInt(firstLine[0]);
        var q = Integer.parseInt(firstLine[1]);
        
        // Store as a mutable byte array
        var s = scanner.nextLine().trim().getBytes();
        
        // Process queries
        for (var i = 0; i < q; i++) {
            var query = scanner.nextLine().split(" ");
            
            switch (query[0]) {
                case "?" -> {
                    // Using text block for clarity and pattern matching
                    var result = new String(s).contains(query[1]) 
                        ? """
                          YES""" 
                        : """
                          NO""";
                    System.out.println(result.trim());
                }
                default -> {
                    var k = Integer.parseInt(query[1]) - 1;
                    s[k] ^= 1;
                }
            }
        }
        
        scanner.close();
    }
}