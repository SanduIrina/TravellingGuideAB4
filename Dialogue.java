

public final class Dialogue {
    public static void sayHello() {
        System.out.println("Welcome traveller!");
        System.out.println("I am here to assist you through your quest");
        System.out.println("However I'm just a demo so I have limited powers");
        System.out.println("I can offer you the following information:");
        System.out.println("1. I can give you all information about a certain location");
        System.out.println("2. I can give you top 5 locations from a certain country/city which are most price convenient"
                + " for a certain period of time");
        System.out.println("3. I can tell you the cheapest place to go do an activity for 10 days");
        System.out.println("4. Exit");
    }
    
    public static void option1() {
        System.out.println("Please insert location name (the list of locations is given below, the name must match it exactly");
    }
    
    public static void option2() {
        System.out.println("Please insert filtering option(city/country):");
    }
    
    public static void option3() {
        System.out.println("Please insert activity name (the list of activities is given below, the name must match it exactly)");
    }
    
    public static void dates() {
        System.out.println("Please insert the timeframe in which you want to visit: startDay startMonth endDay endMonth");
    }
}
