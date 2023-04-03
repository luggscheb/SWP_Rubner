package Push;
public interface MessPunkt {

    public void hinzufügen(Anzeige ob);
    public void löschen(Anzeige ob);

    public void TemperaturMessen(int temp);
    public void LuftfeuchtigkeitMessen(int luft);

    public void ObserverSchicken();

}
