package com.dissan.model;

import com.dissan.model.stuff.Inventory;

import java.util.Map;

public class Character {
    private String name;
    private Race race;
    private CharacterClass characterClass;
    private Inventory inventory;
    private Map<Stats, Integer> statsMap;
    public Character(String name, Race race, CharacterClass characterClass, Inventory inventory, Map<Stats, Integer> statsMap) {
        this.name = name;
        this.race = race;
        this.characterClass = characterClass;
        this.inventory = inventory;
        this.statsMap = statsMap;
    }


}
