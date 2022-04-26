fun main() {
    with(System.`in`.bufferedReader()) {
        val (n, m) = readLine().split(" ").map { it.toInt() }

        val maps = Array(n + 2) { Array(m + 2) { false } }

        for (yi in 1..n) {
            readLine().toList().forEachIndexed { xi, c ->
                maps[yi][xi + 1] = c == '0'
            }
        }

        var result = 0

        for (y in 1..n) {
            for (x in 1..m) {
                if (maps[y][x]) {
                    bfs(maps, y, x)
                    result += 1
                }
            }
        }

        print(result)
    }
}

fun selectionSort(array: List<Int>) {
    for (i in 0 until array.size) {

    }
}