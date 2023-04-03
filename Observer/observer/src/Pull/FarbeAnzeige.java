package Pull;

public class FarbeAnzeige implements Anzeige{

    private String name;
    private MessPunkt messPunkt;

    public FarbeAnzeige(String name){
        this.name = name;
    }

    @Override
    public void aktualisieren() {
        int[] werte = (int[]) messPunkt.bekommeAktualisierung(this);
        if(werte == null){
            System.out.println("Keine neuen Werte!");
        }else{
            if(werte[0] < 20) System.out.print("Luft: Rot ");
            if(werte[0] >= 20) System.out.print("Luft: Grün ");
            if(werte[1] <= 0) System.out.println("Temp: BLAU");
            if(werte[1] > 0) System.out.println("Temp: ORANGE");
        }    
    }

    @Override
    public void setzeMessPunkt(MessPunkt mp) {
       this.messPunkt = mp;
    }
}
