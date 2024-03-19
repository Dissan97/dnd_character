package com.dissan.model.stuff;

public abstract class Item {

    private String name;
    private String description;
    private GoldValue value;

    private int weight;
    public Item(String name, String description, GoldValue value, int weight) {
        this.name = name;
        this.description = description;
        this.value = value;
        this.weight = weight;
    }

    public int getWeight() {
        return this.weight;
    }
}
