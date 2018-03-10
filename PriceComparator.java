import java.util.Comparator;

public class PriceComparator implements Comparator<Destination> {

    @Override
    public int compare(Destination o1, Destination o2) {
        if(o1.getAvgPrice() > o2.getAvgPrice())
            return 1;
        else if(o1.getAvgPrice() < o2.getAvgPrice())
            return -1;
        else return 0;
    }

}
