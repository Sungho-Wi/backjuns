fun main() {
    with(System.`in`.bufferedReader()) {
        val (n, m, k) = readLine().split(" ").map { it.toInt() }
        var numberList = readLine().split(" ").map { it.toInt() }

        numberList = numberList.sortedDescending()

        var count = (m / (k + 1)) * k
        count += m % (k + 1)

        print((numberList.first() * count) + (numberList[1] * (m - count)))

    }
}