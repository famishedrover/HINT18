package com.example.architgoyal.hint18;

/**
 * Created by architgoyal on 17/03/18.
 */

import android.util.Pair;
import java.util.ArrayList;

public class ImageList {
    public static ArrayList<Pair<String,ArrayList<Integer>>> textimage=new ArrayList<Pair<String,ArrayList<Integer>>>();
    public static ArrayList<Integer> apple=new ArrayList<Integer>();
    public static ArrayList<Integer> mango=new ArrayList<Integer>();
    public static ArrayList<Integer> dog=new ArrayList<Integer>();
    public static ArrayList<Integer> cat=new ArrayList<Integer>();
    public static ArrayList<Integer> house=new ArrayList<Integer>();
    public static void set(){
        apple.add(R.drawable.apple1);
        apple.add(R.drawable.apple2);
        apple.add(R.drawable.apple3);
        mango.add(R.drawable.mango1);
        mango.add(R.drawable.mango2);
        mango.add(R.drawable.mango3);
        cat.add(R.drawable.cat1);
        cat.add(R.drawable.cat2);
        cat.add(R.drawable.cat3);
        house.add(R.drawable.house1);
        house.add(R.drawable.house2);
        house.add(R.drawable.house3);
        dog.add(R.drawable.dog1);
        dog.add(R.drawable.dog2);
        dog.add(R.drawable.dog3);
        textimage.add(Pair.create("Dog",dog));
        textimage.add(Pair.create("Cat",cat));
        textimage.add(Pair.create("Apple",apple));
        textimage.add(Pair.create("House",house));
        textimage.add(Pair.create("Mango",mango));

    }
}
