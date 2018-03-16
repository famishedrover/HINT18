package com.example.architgoyal.hint18;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.CardView;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    private CardView mAlpha;
    private CardView mWords;
    private CardView mScan;
    private CardView mRead;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        getSupportActionBar().setTitle("Home");
        mAlpha=(CardView)findViewById(R.id.card_view1);
        mWords=(CardView)findViewById(R.id.card_view2);
        mScan=(CardView)findViewById(R.id.card_view3);
        mRead=(CardView)findViewById(R.id.card_view4);

        mAlpha.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MainActivity.this,alphaPacksActivity.class));
            }
        });
        mWords.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MainActivity.this,wordsPacksActivity.class));
            }
        });
        mScan.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MainActivity.this,scanActivity.class));
            }
        });
        mRead.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MainActivity.this,readActivity.class));
            }
        });
    }
}
