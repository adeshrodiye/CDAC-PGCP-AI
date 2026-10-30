    class GFG {

        // Function to print Armstrong numbers
        static void armstrongNumbers(int start, int end) {

            for (int num = start; num <= end; num++) {

                int original = num;
                int temp = num;

                // Count number of digits
                int digits = 0;
                while (temp != 0) {
                    digits++;
                    temp /= 10;
                }

                temp = num;
                int sum = 0;

                // Calculate sum of digits raised to power 'digits'
                while (temp != 0) {
                    int digit = temp % 10;
                    sum += (int) Math.pow(digit, digits);
                    temp /= 10;
                }

                // Check Armstrong number
                if (sum == original) {
                    System.out.print(original + " ");
                }
            }
        }

        public static void main(String[] args) {

            int start = 100;
            int end = 500;

            System.out.print("Armstrong numbers: ");
            armstrongNumbers(start, end);
        }
    }

