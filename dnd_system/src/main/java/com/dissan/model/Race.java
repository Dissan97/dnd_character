package com.dissan.model;

import org.json.JSONObject;

public class Race {

    private final String name;
    private final JSONObject raceData;


    public Race(String name, JSONObject raceData) {
        this.name = name;
        this.raceData = raceData;
    }

    public String getName() {
        return name;
    }

    public JSONObject getRaceData() {
        return raceData;
    }
}
