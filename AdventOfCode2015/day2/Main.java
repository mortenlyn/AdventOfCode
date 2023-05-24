package AdventOfCode2015.day2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Scanner;

public class Main {
    Collection<String> list = new ArrayList<>();

     public void readFile(String filename) throws FileNotFoundException {
        File file = new File(filename);
        Scanner scanner = new Scanner(file);
        
        while (scanner.hasNextLine()) {
            list.add(scanner.nextLine());
        }
        
        scanner.close();        
     }

     public int expressionPaper(int l, int w, int h) {
         int lw = l*w;
         int lh = l*h;
         int wh = w*h;
         int smallestSide = Math.min(Math.min(lh, wh), lw);

        return (2*l*w + 2*w*h + 2*h*l) + smallestSide;
     }

     public int expressionRibbon(int l, int w, int h) {
        int smallest = Math.min(Math.min(l, w), h);
        int secondSmallest;
        secondSmallest = ((smallest == l) ? Math.min(w, h) : ((smallest == w) ? Math.min(l, h) : Math.min(w, l)));

        int wrap = (2*smallest) + (2*secondSmallest);
        int bow = l*w*h;
        return (wrap + bow);
     }

     public void solve() {
        int totalSquareFeet = 0;
        int totalFeetOfRibbon = 0;
        List<Integer> lengthList = new ArrayList<>();
        List<Integer> widthList = new ArrayList<>();
        List<Integer> heightList = new ArrayList<>();

        for (String line : list) {
            String [] mesures = line.split("x");
            lengthList.add(Integer.valueOf(mesures[0]));
            widthList.add(Integer.valueOf(mesures[1]));
            heightList.add(Integer.valueOf(mesures[2]));
        }

        for (int i = 0; i < lengthList.size(); i++) {
            totalSquareFeet += expressionPaper(lengthList.get(i), widthList.get(i), heightList.get(i));
            totalFeetOfRibbon += expressionRibbon(lengthList.get(i), widthList.get(i), heightList.get(i));
        }

        System.out.println("Part 1: " + totalSquareFeet + "\n" + "Part 2: " + totalFeetOfRibbon);
     }

     public static void main(String[] args) {
        Main main = new Main();
        try {
            main.readFile("AdventOfCode2015/day2/input.txt");
        }
        catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        main.solve();
     }
}
