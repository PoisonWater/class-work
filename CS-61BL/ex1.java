public class StringTest {
    public static void drawTriangle(int n){
        int t1 = 0, t2 = 0;
        while (t1 < n){
           while (t2 < t1) {
              System.out.print("*");
              t2 += 1;
           }
           System.out.println("*");
           t1 = t1 + 1;
           t2 = 0;
        }
    }
    public static void main(String[] args) {
        drawTriangle(5);
    }
 }