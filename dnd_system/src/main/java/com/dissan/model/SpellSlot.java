package com.dissan.model;

public class SpellSlot {
    private int[][] maxSpellSlot;
    private int[][] currentSpellSlot;
    private int level;
    public SpellSlot(int[][] maxSpellSlot, int[][] currentSpellSlot, int level) {
        this.maxSpellSlot = maxSpellSlot;
        this.currentSpellSlot = currentSpellSlot;
    }
}
