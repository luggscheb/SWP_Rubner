public abstract class Pizzeria{
   
   public Pizza holePizza(String welchePizza) {
      Pizza pizza = stellePizzaHer(welchePizza);
      return pizza;
   }
   protected abstract Pizza stellePizzaHer(String welchePizza);
}
