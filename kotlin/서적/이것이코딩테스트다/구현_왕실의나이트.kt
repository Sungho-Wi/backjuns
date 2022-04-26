fun main() {
    with(System.`in`.bufferedReader()) {
        val position = readLine()

        val y = position[0].code - 'a'.code + 1
        val x = position[1].digitToInt()

        val movingList = listOf(-1 to 2, 1 to 2, 2 to -1, 2 to 1, -1 to -2, 1 to -2, -2 to -1, -2 to 1)

        var result = 0

        for ((movingY, movingX) in movingList) {
            if (y + movingY in 1..8 && x + movingX in 1..8) {
                result += 1
            }
        }

        print(result)
    }
}
