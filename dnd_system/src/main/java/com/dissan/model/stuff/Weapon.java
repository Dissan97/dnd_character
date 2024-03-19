package com.dissan.model.stuff;

public class Weapon extends Item{

    private String damage;

    public Weapon(String name, String description, GoldValue value, int weight, String damage) {
        super(name, description, value, weight);
        this.damage = damage;
    }
}
