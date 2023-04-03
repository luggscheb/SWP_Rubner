package Push;
public class BildschirmAnzeige implements Anzeige {

    private String name;
    private MessPunkt messPunkt;

    public BildschirmAnzeige(String name){
        this.name = name;
    }

    @Override
    public void aktualisieren(int[] Messwerte) {
        if(Messwerte == null){
            System.out.println("Keine neue Werte!");

        }else{
            System.out.println("Luft: "+ Messwerte[0] +" Temp: "+ Messwerte[1]);
        }
    }

    @Override
    public void setzeMessPunkt(MessPunkt mp) {
        this.messPunkt = mp;
    }
    
}
