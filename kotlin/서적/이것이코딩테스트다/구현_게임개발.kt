fun main() {
    with(System.`in`.bufferedReader()) {
        val (n, m) = readLine().split(" ").map { it.toInt() }

        var (y, x, direction) = readLine().split(" ").map { it.toInt() }

        y += 1
        x += 1

        val maps = Array(n + 2) { Array(m + 2) { 0 } }

        for (yi in 1..n) {
            readLine().split(" ").forEachIndexed { xi, s ->
                maps[yi][xi + 1] = (s.toInt() + 1) % 2
            }
        }

        var result = 1

        while (true) {
            maps[y][x] = 2
            var isMoved = false

            for (i in 0 until 4) {
                direction = (direction + 3) % 4

                val moved = when (direction) {
                    0 -> y - 1 to x
                    1 -> y to x + 1
                    2 -> y + 1 to x
                    else -> y to x - 1
                }

                if (maps[moved.first][moved.second] == 1) {
                    y = moved.first
                    x = moved.second
                    isMoved = true
                    result += 1
                    break
                }
            }

            if (!isMoved) {
                val moved = when (direction) {
                    0 -> y + 1 to x
                    1 -> y to x - 1
                    2 -> y - 1 to x
                    else -> y to x + 1
                }

                if (maps[moved.first][moved.second] != 0) {
                    y = moved.first
                    x = moved.second
                } else {
                    break
                }
            }
        }

        print(result)
    }
}
