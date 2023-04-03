package Push;

public class FarbeAnzeige implements Anzeige{

    private String name;
    private MessPunkt messPunkt;

    public FarbeAnzeige(String name){
        this.name = name;
    }

    @Override
    public void aktualisieren(int[] Messwerte) {
        if(Messwerte == null){
            System.out.println("Keine neuen Werte!");
        }else{
            if(Messwerte[0] < 20) System.out.print("Luft: Rot ");
            if(Messwerte[0] >= 20) System.out.print("Luft: Grün ");
            if(Messwerte[1] <= 0) System.out.println("Temp: BLAU");
            if(Messwerte[1] > 0) System.out.println("Temp: ORANGE");
        }    
    }

    @Override
    public void setzeMessPunkt(MessPunkt mp) {
       this.messPunkt = mp;
    }
}
