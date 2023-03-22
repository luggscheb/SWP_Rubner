public interface MessPunkt {

    public void hinzufügen(Observer ob);
    public void löschen(Observer ob);

    public void TemperaturMessen(int temp);
    public void LuftfeuchtigkeitMessen(int luft);

    public void ObserverSchicken();
    public Object bekommeAktualisierung(Observer ob);

}
