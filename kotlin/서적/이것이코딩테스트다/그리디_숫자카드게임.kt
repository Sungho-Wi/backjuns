fun main() {
    with(System.`in`.bufferedReader()) {
        val (n, m) = readLine().split(" ").map { it.toInt() }

        val cards = mutableListOf<List<Int>>()

        for (i in 0 until n) {
            cards.add(readLine().split(" ").map { it.toInt() })
        }

        var result = 0

        for (i in 0 until n) {
            val rowMinValue = cards[i].minOrNull()!!
            if (result < rowMinValue) {
                result = rowMinValue
            }
        }

        print(result)
    }
}
