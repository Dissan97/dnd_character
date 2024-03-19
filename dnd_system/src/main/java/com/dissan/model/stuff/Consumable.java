package com.dissan.model.stuff;

public class Consumable extends Item{

    private String effect;

    public Consumable(String name, String description, GoldValue value, int weight, String effect) {
        super(name, description, value, weight);
        this.effect = effect;
    }

}
