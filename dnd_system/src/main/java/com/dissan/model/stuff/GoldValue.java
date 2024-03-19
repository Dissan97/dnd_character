package com.dissan.model.stuff;

public class GoldValue {

    private GoldType goldType;
    private int amount;

    public GoldValue(GoldType goldType, int amount) {
        this.goldType = goldType;
        this.amount = amount;
    }

    public enum GoldType{
        BRONZE,
        SILVER,
        GOLD,
        PLATINUM

    }
}
