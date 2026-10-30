package Ecommerce;

import java.util.List;

public class TestECommerce {

    public static void main(String[] args) {
        populateInventory();
    }
    private static void populateInventory() {

        InventoryManagement inventory = new InventoryManagement();
        inventory.addInInventory(new Product(1,
                "Laptop", 50000, 5));
        inventory.addInInventory(new Product(2,
                "Phone", 20000, 10));

        inventory.printStock();

        User user1 = new User("Aashish", 1);
        List<Product> products = user1.getProducts();
        products.add(new Product(1, "Laptop",
                50000, 1));
        products.add(new Product(2, "Phone",
                20000, 1));

        try {

            inventory.checkout(products);
            System.out.println(" Checkout successful!");
        } catch (InventoryException e) {
            System.out.println(e.getMessage());
        }

        inventory.printStatistics();
    }

}