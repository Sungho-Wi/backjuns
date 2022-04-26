fun main() {
    with(System.`in`.bufferedReader()) {
        val n = readLine().toInt()
        val movingList = readLine().split(" ")

        var currentY = 1
        var currentX = 1

        for (moving in movingList) {
            var movedX = currentX
            var movedY = currentY
            when (moving) {
                "L" -> movedX -= 1
                "R" -> movedX += 1
                "U" -> movedY -= 1
                "D" -> movedY += 1
            }

            if (movedY in 1 .. n) {
                currentY = movedY
            }
            if (movedX in 1 .. n) {
                currentX = movedX
            }
        }

        print("$currentY $currentX")
    }
}
