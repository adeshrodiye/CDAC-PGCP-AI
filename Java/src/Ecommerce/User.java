package Ecommerce;

import java.util.ArrayList;
import java.util.List;

public class User {
    private String name;
    private double user_id;
    private List<Product> products = new ArrayList<>();

    public User(String name, double user_id) {
        this.name = name;
        this.user_id = user_id;
    }

    public List<Product> getProducts() {
        return products;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getUser_id() {
        return user_id;
    }

    public void setUser_id(double user_id) {
        this.user_id = user_id;
    }
}