package Ecommerce;
import java.util.*;
public class InventoryManagement {
    private Map<Integer, Product> stock = new HashMap<>();
    private Map<Integer, Integer> soldStats = new HashMap<>();
    public void printStock(){
        System.out.println(stock.keySet());
    }
    public void checkout(List<Product> cart) throws InventoryException {
        for (Product product : cart) {
            Product invItem = stock.get(product.getId());
            if (invItem == null || invItem.getQuantity() < 1) {
                throw new InventoryException("Product not available: " + product.getProduct_name());
            }
            if(invItem.getQuantity() >= product.getQuantity())
                invItem.setQuantity(invItem.getQuantity()
                        - product.getQuantity());
            else
                throw new InventoryException(
                        "Quantity in-sufficient for " +
                                "Inventory Product: " +
                                product.getProduct_name() +
                                " Available Quantity -> " +
                                invItem.getQuantity());

            soldStats.put(product.getId(),
                    soldStats.getOrDefault(
                            product.getId(), 0) +
                            product.getQuantity());
        }
    }
    public void printStatistics() {
        System.out.println(" Sales Statistics:");
        soldStats.forEach((id, count) -> {
            Product product = stock.get(id);
            System.out.println(product.getProduct_name() +
                    " sold: " + count +
                    ", remaining: " + product.getQuantity());
        });
    }
    public void addInInventory(Product product){
        stock.put(product.getId(), product);
    }
}