package com.example.architgoyal.hint18;

/**
 * Created by architgoyal on 17/03/18.
 */
import android.support.v7.widget.CardView;

public interface CardAdapter {

    int MAX_ELEVATION_FACTOR = 8;

    float getBaseElevation();

    CardView getCardViewAt(int position);

    int getCount();
}