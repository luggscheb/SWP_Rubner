package Pull;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;

import javax.swing.event.ChangeEvent;

public class MessPunktInnsbruck implements MessPunkt{

    private List<Anzeige> observers;
    private int Temperatur;
    private int Luftfeuchtigkeit;
    private boolean verändert;
    private final Object MUTEX = new Object();


    public MessPunktInnsbruck(){
            this.observers = new ArrayList<>();
    }


    @Override
    public void hinzufügen(Anzeige ob) {
       if(ob == null) throw new NullPointerException("Kein Observer");
       synchronized (MUTEX){
        if(!observers.contains(ob)) observers.add(ob);
       }
    }

    @Override
    public void löschen(Anzeige ob) {
       synchronized(MUTEX){
        observers.remove(ob);
       }
    }

    @Override
    public void TemperaturMessen(int temp) {
        System.out.println("Temperatur gemessen: "+ Integer.toString(temp));
        this.Temperatur = temp;
        this.verändert = true;
        ObserverSchicken();

    }

    @Override
    public void LuftfeuchtigkeitMessen(int luft) {
        System.out.println("Luftfeuchtigkeit gemessen: "+ Integer.toString(luft));
        this.Luftfeuchtigkeit = luft;
        this.verändert = true;
        ObserverSchicken();
    }

    @Override
    public void ObserverSchicken() {
        List <Anzeige> observersLokal = null;
        synchronized (MUTEX){
            if(!verändert)
            return;
            observersLokal = new ArrayList<>(this.observers);
            this.verändert = false;
        }
        for (Anzeige obj : observersLokal){
            obj.aktualisieren();
        }
    }


    @Override
    public Object bekommeAktualisierung(Anzeige ob) {
        int[] rückgabe = {this.Luftfeuchtigkeit, this.Temperatur}; 
        return rückgabe;
    }


    
}
