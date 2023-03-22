public class App {
    public static void main(String[] args) throws Exception {
        MessPunkt mp = new MessPunktInnsbruck();

        Observer o1 = new BildschirmAnzeige("B1");
        Observer o2 = new BildschirmAnzeige("B2");
        Observer o3 = new FarbeAnzeige("F1");

        mp.hinzufügen(o1);
        mp.hinzufügen(o2);
        mp.hinzufügen(o3);

        o1.setzeMessPunkt(mp);
        o2.setzeMessPunkt(mp);
        o3.setzeMessPunkt(mp);

        o1.aktualisieren();

        mp.LuftfeuchtigkeitMessen(15);
        mp.TemperaturMessen(20);
    }
}
