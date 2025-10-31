public class AlphabetPosition {
    public static int getPosition(char letter) {
        return Character.toUpperCase(letter) - 'A' + 1;
    }

    public static void main(String[] args) {
        System.out.println(getPosition('C')); // Output: 3
        System.out.println(getPosition('z')); // Output: 26
    }
}
