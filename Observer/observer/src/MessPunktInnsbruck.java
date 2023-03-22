import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;

import javax.swing.event.ChangeEvent;

public class MessPunktInnsbruck implements MessPunkt{

    private List<Observer> observers;
    private int Temperatur;
    private int Luftfeuchtigkeit;
    private boolean verändert;
    private final Object MUTEX = new Object();


    public MessPunktInnsbruck(){
            this.observers = new ArrayList<>();
    }


    @Override
    public void hinzufügen(Observer ob) {
       if(ob == null) throw new NullPointerException("Kein Observer");
       synchronized (MUTEX){
        if(!observers.contains(ob)) observers.add(ob);
       }
    }

    @Override
    public void löschen(Observer ob) {
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
        List <Observer> observersLokal = null;
        synchronized (MUTEX){
            if(!verändert)
            return;
            observersLokal = new ArrayList<>(this.observers);
            this.verändert = false;
        }
        for (Observer obj : observersLokal){
            obj.aktualisieren();
        }
    }


    @Override
    public Object bekommeAktualisierung(Observer ob) {
        int[] rückgabe = {this.Luftfeuchtigkeit, this.Temperatur}; 
        return rückgabe;
    }


    
}
