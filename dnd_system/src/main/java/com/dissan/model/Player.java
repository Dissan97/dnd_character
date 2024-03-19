package com.dissan.model;

import java.util.ArrayList;
import java.util.List;

public class Player {

    private List<Character> characterList;
    private final String username;
    private final String password;

    public Player(List<Character> characterList, String username, String password) {
        this.characterList = characterList;
        this.username = username;
        this.password = password;
    }

    public Player(String username, String password) {
        this.username = username;
        this.password = password;
        this.characterList = new ArrayList<>();
    }

    public List<Character> getCharacterList() {
        return characterList;
    }

    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }

    public void setCharacterList(List<Character> characterList) {
        this.characterList = characterList;
    }
}
