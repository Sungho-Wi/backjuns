import java.text.DecimalFormat

fun main() {
    with(System.`in`.bufferedReader()) {
        val (n, k) = readLine().split(" ").map { it.toInt() }

        val charK = k.digitToChar()

        /*
        그리디로 풀었을 경우

        val result = if (n < 3) {
            1575 * (n + 1)
        } else if (n in 3 until 13) {
            1575 * n + 3600
        } else if (n in 13 until 23) {
            1575 * (n - 1) + (3600 * 2)
        } else {
            1575 * (n - 2) + (3600 * 3)
        }

        print(result)
        */

        var result = 0

        val df = DecimalFormat("00")

        for (second in 0 until 60) {
            for (minute in 0 until 60) {
                for (hour in 0 .. n) {
                    if (charK in "${df.format(hour)}${df.format(minute)}${df.format(second)}") {
                        result += 1
                    }
                }
            }
        }

        print(result)
    }
}
