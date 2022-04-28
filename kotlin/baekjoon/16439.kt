import kotlin.math.max

fun main() {
    with(System.`in`.bufferedReader()) {
        val (n, m) = readLine().split(" ").map { it.toInt() }

        val chickens = mutableListOf<List<Int>>()

        for (i in 0 until n) {
            chickens.add(readLine().split(" ").map { it.toInt() })
        }

        val combinations = combine((0 until m).toList(), limit = 3)

        var answer = Int.MIN_VALUE

        combinations.forEach { (a, b, c) ->
            var result = 0
            for (i in 0 until n) {
                result += listOf(chickens[i][a], chickens[i][b], chickens[i][c]).maxOrNull()!!
            }
            answer = max(answer, result)
        }

        print(answer)
    }
}

fun <T> combine(el: List<T>, limit: Int = el.size, fin: List<T> = listOf(), index: Int = 0): List<List<T>> {
    return if (fin.size >= limit) {
        listOf(fin)
    } else {
        el.slice(index until el.size).flatMapIndexed { i: Int, t: T -> combine(el, limit, fin + t, index + i + 1) }
    }
}