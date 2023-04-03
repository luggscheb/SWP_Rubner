public abstract class Pizza {

   public abstract String getSorte();
   public abstract int getPrice();

   public void herstellen(){
      backen();
      schneiden();
      einpacken();
      System.out.println("Das macht dann:" + getPrice() + "EUR");
   }

   public void backen(){
      System.out.println("backe: " + getSorte());
   }
   public void schneiden(){
      System.out.println("schneide: " + getSorte());
   }
   public void einpacken(){
      System.out.println("einpacken: " + getSorte());
   }
}
