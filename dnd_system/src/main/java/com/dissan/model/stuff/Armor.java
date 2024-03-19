package com.dissan.model.stuff;

public class Armor extends Item{
    private int armorClass;

    public Armor(String name, String description, GoldValue value, int weight, int armorClass) {
        super(name, description, value, weight);
        this.armorClass = armorClass;
    }
}
