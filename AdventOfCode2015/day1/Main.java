package AdventOfCode2015.day1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


public class Main {
    private char[] charArray;

    public char[] readFile() throws FileNotFoundException {
        File input = new File("AdventOfCode2015/day1/input.txt");
        Scanner scanner = new Scanner(input);

        while (scanner.hasNextLine()) {
            String data = scanner.nextLine();
            charArray = data.toCharArray();

        }
        scanner.close();
        return charArray;
    }

    public int solve() {
        int floor = 0;
        boolean foundPart2 = false;
        for (int i = 0; i < charArray.length; i++) {
            if (charArray[i] == '(') {
                floor++;
            } else if (charArray[i] == ')') {
                floor--;
                if (floor == -1 && foundPart2 == false) {
                    System.out.println("Part 2: " + (i+1));
                    foundPart2 = true;
                }
            }
        }   
        return floor;
    }

    public static void main(String[] args) {
        Main main = new Main();
        try {
            main.readFile();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        System.out.println(main.solve());
    }
}
