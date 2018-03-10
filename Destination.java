import java.util.List;
import java.util.ArrayList;
public class Destination {
    private String name;
    private String city;
    private String coutry;
    private int avgPrice;
    private List<String> activ = new ArrayList<String>();
    private int startDay;
    private int startMonth;
    private int endDay;
    private int endMonth;
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getCity() {
        return city;
    }
    public void setCity(String city) {
        this.city = city;
    }
    public int getAvgPrice() {
        return avgPrice;
    }
    public void setAvgPrice(int avgPrice) {
        this.avgPrice = avgPrice;
    }
    public List<String> getActiv() {
        return activ;
    }
    public void addActiv(String newActiv) {
        activ.add(newActiv);
    }
    public int getStartDay() {
        return startDay;
    }
    public void setStartDay(int startDay) {
        this.startDay = startDay;
    }
    public int getStartMonth() {
        return startMonth;
    }
    public void setStartMonth(int startMonth) {
        this.startMonth = startMonth;
    }
    public int getEndDay() {
        return endDay;
    }
    public void setEndDay(int endDay) {
        this.endDay = endDay;
    }
    public int getEndMonth() {
        return endMonth;
    }
    public void setEndMonth(int endMonth) {
        this.endMonth = endMonth;
    }
    public String getCoutry() {
        return coutry;
    }
    public void setCoutry(String coutry) {
        this.coutry = coutry;
    }
}
