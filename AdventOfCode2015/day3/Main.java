package AdventOfCode2015.day3;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

public class Main {
    private Set<Coords> coordsSanta = new HashSet<>();
    private List<String> stringList = new ArrayList<>();
    private int x1 = 0, y1 = 0, x2 = 0, y2 = 0;

    public void readFile(String filname) throws FileNotFoundException {
        File file = new File(filname);
        Scanner scanner = new Scanner(file);

        while (scanner.hasNextLine()) {
            stringList.add(scanner.nextLine());
        }
        scanner.close();
    }

    private void updateCoordinates(String direction, int counter) {
        int x, y;
    
        if (counter % 2 == 0) {
            x = this.x1;
            y = this.y1;
        } else {
            x = this.x2;
            y = this.y2;
        }
    
        switch (direction) {
            case "^":
                y++;
                break;
            case "v":
                y--;
                break;
            case "<":
                x--;
                break;
            case ">":
                x++;
                break;
            default:
                // Handle invalid input
                break;
        }
    
        if (counter % 2 == 0) {
            this.x1 = x;
            this.y1 = y;
            coordsSanta.add(new Coords(x1, y1));
        } else {
            this.x2 = x;
            this.y2 = y;
            coordsSanta.add(new Coords(x2, y2));
        }
    }

    public int findHouses() {
        String[] input = stringList.get(0).split("");
        int counter = 0;
    
        for (int i = 0; i < input.length; i++) {
            updateCoordinates(input[i], counter);
            counter++;
        }

        return coordsSanta.size();
    }

    @Override
    public String toString() {
        return "Main [coordsSanta=" + coordsSanta + "]";
    }

    public static void main(String[] args) {
        Main main = new Main();
        try {
            main.readFile("AdventOfCode2015/day3/input.txt");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        System.out.println(main.findHouses());
    }
}