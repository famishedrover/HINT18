package com.example.architgoyal.hint18;

import android.content.Intent;
import android.support.v4.view.ViewPager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class wordsPacksActivity extends AppCompatActivity {

    private ViewPager mViewPager;
    private CardPagerAdapterWords mCardAdapter;
    private ShadowTransformer mCardShadowTransformer;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_words_packs);
        getSupportActionBar().setTitle("Choose Packs");

        mViewPager = (ViewPager) findViewById(R.id.viewPager);
        mCardAdapter = new CardPagerAdapterWords();
        mCardAdapter.addCardItem(new CardItem("Pack of 5"));
        mCardAdapter.addCardItem(new CardItem("Pack of 10"));
        mCardAdapter.addCardItem(new CardItem("Pack of 15"));
        mCardAdapter.addCardItem(new CardItem("Pack of 20"));
        mCardShadowTransformer = new ShadowTransformer(mViewPager, mCardAdapter);
        mCardShadowTransformer.enableScaling();
        mViewPager.setAdapter(mCardAdapter);
        mViewPager.setPageTransformer(false, mCardShadowTransformer);
    }
}
