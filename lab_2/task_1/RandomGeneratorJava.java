import java.security.SecureRandom;

/**
 * Class generates a pseudorandom binary sequence
 */
public class RandomGeneratorJava {

    public static void main(String[] args) {
        int length = 128;
        String binarySequence = generateRandomBinarySequence(length);
        System.out.println("Псевдослучайная бинарная последовательность: " + binarySequence);
    }

    /**
     * Generate a pseudorandom binary sequence of the specified length
     * @param length Length of the binary sequence in bits
     * @return String of binary sequence
     */
    private static String generateRandomBinarySequence(int length) {
        SecureRandom secureRandom = new SecureRandom();
        StringBuilder binaryStringBuilder = new StringBuilder();

        for (int i = 0; i < length; i++) {
            int bit = secureRandom.nextInt(2);
            binaryStringBuilder.append(bit);
        }

        return binaryStringBuilder.toString();
    }
}
