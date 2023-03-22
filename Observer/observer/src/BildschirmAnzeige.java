public class BildschirmAnzeige implements Observer {

    private String name;
    private MessPunkt messPunkt;

    public BildschirmAnzeige(String name){
        this.name = name;
    }

    @Override
    public void aktualisieren() {
        int[] werte = (int[]) messPunkt.bekommeAktualisierung(this);
        if(werte == null){
            System.out.println("Keine neue Werte!");

        }else{
            System.out.println("Luft: "+ werte[0] +" Temp: "+ werte[1]);
        }
    }

    @Override
    public void setzeMessPunkt(MessPunkt mp) {
        this.messPunkt = mp;
    }
    
}
