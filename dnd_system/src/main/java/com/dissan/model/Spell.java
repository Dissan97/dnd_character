package com.dissan.model;

import java.util.List;

public class Spell {

    private final String name;
    private final int level;
    private final String distance;
    private final String components;
    private final String duration;
    private final String description;
    private final String school;
    private final List<ClassType> availableClass;
    private  boolean isRitual;
    private  boolean isConcentration;
    private final String castingTime;

    public Spell(String name, int level, String distance, String components, String duration, String description,
                 String school, List<ClassType> availableClass, boolean isRitual, boolean isConcentration,
                 String castingTime) {
        this.name = name;
        this.level = level;
        this.distance = distance;
        this.components = components;
        this.duration = duration;
        this.description = description;
        this.school = school;
        this.availableClass = availableClass;
        this.isRitual = isRitual;
        this.isConcentration = isConcentration;
        this.castingTime = castingTime;
    }

    public String getName() {
        return name;
    }

    public int getLevel() {
        return level;
    }

    public String getDistance() {
        return distance;
    }

    public String getComponents() {
        return components;
    }

    public String getDuration() {
        return duration;
    }

    public String getDescription() {
        return description;
    }

    public String getSchool() {
        return school;
    }

    public List<ClassType> getAvailableClass() {
        return availableClass;
    }

    public boolean isRitual() {
        return isRitual;
    }

    public boolean isConcentration() {
        return isConcentration;
    }

    public String getCastingTime() {
        return castingTime;
    }

    public void setRitual(boolean ritual) {
        isRitual = ritual;
    }

    public void setConcentration(boolean concentration) {
        isConcentration = concentration;
    }
}
