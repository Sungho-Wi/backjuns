fun main() {
    with(System.`in`.bufferedReader()) {
        var (n, k) = readLine().split(" ").map { it.toInt() }

        var count = 0

        while (n >= k) {
            val remainder = n % k
            n = if (remainder != 0) {
                count += remainder
                n - remainder
            } else {
                count += 1
                n / k
            }
        }

        while (n > 1) {
            count += 1
            n -= 1
        }

        print(count)
    }
}
