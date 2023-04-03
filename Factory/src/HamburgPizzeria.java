public class HamburgPizzeria extends Pizzeria {

   @Override
   protected Pizza stellePizzaHer(String welchePizza) {
      Pizza pizza = null;
      if(welchePizza.equalsIgnoreCase("Salami")){
         pizza = new Salami();
      }else if(welchePizza.equalsIgnoreCase("Hawaii")){
         pizza = new Hawaii();
      }else if(welchePizza.equalsIgnoreCase("Calzone")){
         pizza = new Calzone();
      }else if(welchePizza.equalsIgnoreCase("Quattro Stagioni")){
         pizza = new QuattroStagioni();
      }
      return pizza;
   }
   
}
