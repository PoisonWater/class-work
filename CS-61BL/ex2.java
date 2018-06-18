public class ArrayMax {
    /** Returns the maximum value from arr. */
    public static int max(int[] arr) {
        int t = arr[0];
        int length = arr.length;
        int p = 0;
        while (p != length - 1){
            p = p + 1;
            if (arr[p] > t)
                t = arr[p];
        }
        return t;
    }
    public static void main(String[] args) {
        int[] numbers = new int[]{9, 2, 15, 2, 22, 10, 6};
        System.out.print(max(numbers));
    }
}