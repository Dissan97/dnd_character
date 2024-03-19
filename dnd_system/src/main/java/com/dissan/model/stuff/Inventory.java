package com.dissan.model.stuff;

import java.util.List;

public class Inventory {

    private List<Item> itemList;
    private int weight = 0;

    public void addItem(Item item){
        itemList.add(item);
        weight += item.getWeight();
    }
    public void removeItem(Item item){
        itemList.remove(item);
        weight += item.getWeight();
    }
    private void setWeight() {
    }
}
