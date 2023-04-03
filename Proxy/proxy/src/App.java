public class App {
    public static void main(String[] args) throws Exception {
        DruckerProxy drucker = new DruckerProxy(new DruckerSW());
        drucker.Drucken("Laborbericht.pdf");
        drucker.switchTo("FARBE");
        drucker.Drucken("Laborbericht.pdf");
    }
}
