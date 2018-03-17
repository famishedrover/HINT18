package com.example.architgoyal.hint18;

import android.util.Pair;

import java.util.ArrayList;

/**
 * Created by architgoyal on 17/03/18.
 */

public class CharacterList {
    public static ArrayList<Pair<String,String>> list;

    public static void setList(){
        list.add(Pair.create("A","0"));
        list.add(Pair.create("B","0"));
        list.add(Pair.create("C","0"));
        list.add(Pair.create("D","0"));
        list.add(Pair.create("E","0"));
    }
}
