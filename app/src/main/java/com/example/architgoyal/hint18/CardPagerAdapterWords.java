package com.example.architgoyal.hint18;

import android.content.Intent;
import android.support.v4.view.PagerAdapter;
import android.support.v7.widget.CardView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by architgoyal on 17/03/18.
 */

public class CardPagerAdapterWords extends PagerAdapter implements CardAdapter {

    private List<CardView> mViews;
    private List<CardItem> mData;
    private float mBaseElevation;

    public CardPagerAdapterWords() {
        mData = new ArrayList<>();
        mViews = new ArrayList<>();
    }

    public void addCardItem(CardItem item) {
        mViews.add(null);
        mData.add(item);
    }

    public float getBaseElevation() {
        return mBaseElevation;
    }

    @Override
    public CardView getCardViewAt(int position) {
        return mViews.get(position);
    }

    @Override
    public int getCount() {
        return mData.size();
    }

    @Override
    public boolean isViewFromObject(View view, Object object) {
        return view == object;
    }

    @Override
    public Object instantiateItem(final ViewGroup container, final int position) {
        View view = LayoutInflater.from(container.getContext())
                .inflate(R.layout.adapter_packs, container, false);
        container.addView(view);
        bind(mData.get(position), view);
        CardView cardView = (CardView) view.findViewById(R.id.cardView);

        if (mBaseElevation == 0) {
            mBaseElevation = cardView.getCardElevation();
        }

        cardView.setMaxCardElevation(mBaseElevation * MAX_ELEVATION_FACTOR);
        cardView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(position==0){
                    Intent intent=new Intent(container.getContext(),wordsCanvasActivity.class);
                    container.getContext().startActivity(intent);
                }
                else if(position==1){
                    Intent intent=new Intent(container.getContext(),wordsCanvasActivity.class);
                    container.getContext().startActivity(intent);
                }
                else if(position==2){
                    Intent intent=new Intent(container.getContext(),wordsCanvasActivity.class);
                    container.getContext().startActivity(intent);
                }
                else if(position==3){
                    Intent intent=new Intent(container.getContext(),wordsCanvasActivity.class);
                    container.getContext().startActivity(intent);
                }
            }
        });
        mViews.set(position, cardView);
        return view;
    }

    @Override
    public void destroyItem(ViewGroup container, int position, Object object) {
        container.removeView((View) object);
        mViews.set(position, null);
    }

    private void bind(CardItem item, View view) {
        TextView packs = (TextView) view.findViewById(R.id.pack);
        packs.setText(item.getPack());
    }
}
