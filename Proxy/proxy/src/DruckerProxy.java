public class DruckerProxy implements Drucker {

    private Drucker drucker;


    public DruckerProxy(Drucker d){
        this.drucker = d;
    }

    @Override
    public void Drucken(String Datei) {
        //ckeck if Seite leer
        drucker.Drucken(Datei);
    }
    
    public void switchTo(String druckerName){
        switch (druckerName) {
            case "SW":
                drucker = new DruckerSW();
                break;
        
            case "FARBE":
                drucker = new DruckerSW();
                break;
        }
    }

}
