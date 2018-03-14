import java.util.*;

import java.io.File;
import fSystem.*;
import java.io.IOException;

public class Main {

    public static void main(String[] args) {
        try {
            //reading data from input file
            FileSystem f = new FileSystem(args[0]," ");
            List<Destination> dest = new ArrayList<Destination>();
            int n = f.nextInt();
            
            HashMap<String, ArrayList<Destination>> cities = new HashMap<String, ArrayList<Destination>>();
            HashMap<String, ArrayList<String>> countries = new HashMap<String, ArrayList<String>>();
            
            ArrayList<String> literalCity = new ArrayList<String>();
            ArrayList<String> literalCountry = new ArrayList<String>();
            ArrayList<String> literalActivity = new ArrayList<String>();
            
            for(int i=0; i<n; i++) {
                Destination curr = new Destination();
                curr.setName(f.nextWord());
                String country = f.nextWord();
                if(!literalCountry.contains(country)) {
                    literalCountry.add(country);
                }
                curr.setCoutry(country);
                String city = f.nextWord();
                if(!literalCity.contains(city)) {
                    literalCity.add(city);
                }
                if(countries.containsKey(country)) {
                    if(!countries.get(country).contains(city))
                        countries.get(country).add(city);
                } else {
                    countries.put(country, new ArrayList<String>());
                    countries.get(country).add(city);
                }
                curr.setCity(city);
                curr.setAvgPrice(f.nextInt());
                int nActiv = f.nextInt();
                for(int j=0; j<nActiv; j++) {
                    String activity = f.nextWord();
                    curr.addActiv(activity);
                    if(!literalActivity.contains(activity)) {
                        literalActivity.add(activity);
                    }
                }
                curr.setStartDay(f.nextInt());
                curr.setStartMonth(f.nextInt());
                curr.setEndDay(f.nextInt());
                curr.setEndMonth(f.nextInt());
                dest.add(curr);
                if(cities.containsKey(city)) {
                    if(!cities.get(city).contains(curr));
                        cities.get(city).add(curr);
                } else {
                    cities.put(city, new ArrayList<Destination>());
                    cities.get(city).add(curr);
                }
            }
            //user interraction
            Dialogue.sayHello();
            Scanner sc = new Scanner(System.in);
            int option = 0;
            while(option != 4) {
                System.out.println("Enter option number(1-4):");
                option = sc.nextInt();
                
                switch(option) {
                    case 1: Dialogue.option1();
                            for(int i=0; i<dest.size(); i++) {
                                System.out.println(" " + i + ". " + dest.get(i).getName());
                            }
                            String name = sc.next();
                            int ok=0;
                            for(int i=0; i< dest.size(); i++){
                                if(dest.get(i).getName().equals(name)) {
                                    System.out.println("Your destination is in " + dest.get(i).getCity());
                                    System.out.println("Average price on a day is " + dest.get(i).getAvgPrice());
                                    System.out.println("You can do the following activities there " + dest.get(i).getActiv());
                                    System.out.println("You can go there between the dates " + dest.get(i).getStartDay() + "." + 
                                    dest.get(i).getStartMonth() + " and " + dest.get(i).getEndDay() + "." + dest.get(i).getEndMonth());
                                    ok = 1;
                                }   
                            }
                            if(ok == 0) {
                                System.out.println("Invalid Option");
                            }
                            break;
                            
                    case 2: Dialogue.option2();
                            String criteria = sc.next();
                            Dialogue.dates();
                            int startDay, endDay, startMth, endMth;
                            startDay = sc.nextInt();
                            startMth = sc.nextInt();
                            endDay = sc.nextInt();
                            endMth = sc.nextInt();
                            ArrayList<Destination> result = new ArrayList<Destination>();
                            if(criteria.equals("country")) {
                                System.out.println("Insert a country name from the list below:");
                                for(int i=0; i<literalCountry.size(); i++) {
                                    System.out.println(i + ". " + literalCountry.get(i));
                                }
                                String location = sc.next();
                                if(!literalCountry.contains(location)) {
                                    System.out.println("Invalid Option");
                                }
                                ArrayList<String> C = countries.get(location);
                                for(int i=0; i<C.size(); i++) {
                                    String D = C.get(i);
                                    ArrayList<Destination> dd = cities.get(D);
                                    for(int j=0; j<dd.size(); j++) {
                                        result.add(dd.get(j));
                                    }
                                }
                            } else if(criteria.equals("city")) {
                                System.out.println("Insert a city name from the list below:");
                                for(int i=0; i<literalCity.size(); i++) {
                                    System.out.println(i + ". " + literalCity.get(i));
                                }
                                String location = sc.next();
                                if(!literalCity.contains(location)) {
                                    System.out.println("Invalid Option");
                                }
                                result = cities.get(location);
                                
                            }
                            for(int i=0; i<result.size(); i++) {
                                if(!(startMth >= result.get(i).getStartMonth()
                                   && endMth <= result.get(i).getEndMonth()
                                   && startDay >= result.get(i).getStartDay()
                                   && endDay <= result.get(i).getEndDay())) {
                                    result.remove(i);
                                    i--;
                                }
                            }
                            if(result.size() == 0) {
                                System.out.println("No location available in the requested period");
                            }
                            Collections.sort(result, new PriceComparator());
                            for(int i=0; i<result.size(); i++) {
                                System.out.println("Destination: " + result.get(i).getName() + 
                                        " with an average price/day of " +result.get(i).getAvgPrice());
                            }
                            break;
                            
                    case 3: Dialogue.option3();
                            for(int i=0; i<literalActivity.size(); i++) {
                                System.out.println(i + ". " + literalActivity.get(i));
                            }
                            ArrayList<Destination> acts = new ArrayList<Destination>();
                            String activity = sc.next();
                            if(!literalActivity.contains(activity)) {
                                System.out.println("Invalid Option");
                                break;
                            }
                            for(int i=1; i<dest.size(); i++) {
                                if(dest.get(i).getActiv().contains(activity)) {
                                    acts.add(dest.get(i));
                                }
                            }
                            Collections.sort(acts,new PriceComparator());
                            System.out.println("Most price-convenient destination:");
                            System.out.println(acts.get(0).getName() + ", " + acts.get(0).getCity());                            
                            
                            break;
                    case 4: System.out.println("Goodbye!");
                            break;
                    default: System.out.println("Invalid Option");
                             break;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
