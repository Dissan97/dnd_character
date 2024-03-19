package com.dissan.model;

import java.util.Map;

public class CharacterClass {
    private ClassType classType;
    private Map<Integer, Spell> spellMap;
    private Map<Integer, Spell> activeSpell;
    private SpellSlot spellSlot;

    public CharacterClass(ClassType classType, Map<Integer, Spell> spellMap, Map<Integer, Spell> activeSpell, SpellSlot spellSlot) {
        this.classType = classType;
        this.spellMap = spellMap;
        this.activeSpell = activeSpell;
        this.spellSlot = spellSlot;
    }

    public ClassType getClassType() {
        return classType;
    }

    public void setClassType(ClassType classType) {
        this.classType = classType;
    }

    public Map<Integer, Spell> getSpellMap() {
        return spellMap;
    }

    public void setSpellMap(Map<Integer, Spell> spellMap) {
        this.spellMap = spellMap;
    }

    public Map<Integer, Spell> getActiveSpell() {
        return activeSpell;
    }

    public void setActiveSpell(Map<Integer, Spell> activeSpell) {
        this.activeSpell = activeSpell;
    }

    public SpellSlot getSpellSlot() {
        return spellSlot;
    }

    public void setSpellSlot(SpellSlot spellSlot) {
        this.spellSlot = spellSlot;
    }
}
