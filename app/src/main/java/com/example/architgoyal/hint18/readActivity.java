package com.example.architgoyal.hint18;

import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.speech.RecognizerIntent;
import android.support.v4.util.Pair;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.Spannable;
import android.text.SpannableString;
import android.util.Log;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.Locale;

public class readActivity extends AppCompatActivity {

    private TextView tv;
    private Spannable spannable;
    private String str;
    private ArrayList<Pair<String,Integer>> wordsList;
    private final int REQ_CODE_SPEECH_INPUT = 100;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_read);
        getSupportActionBar().setTitle("Read & Speak");

        tv=(TextView)findViewById(R.id.text_view);
        str=tv.getText().toString();
        spannable = new SpannableString(str);
        createWordsList();
        promptSpeechInput();
    }

    public void createWordsList(){
        wordsList=new ArrayList<Pair<String,Integer>>();

        int i=0;
        while(i<str.length()){
            String temp="";
            while(i<str.length()&&(str.charAt(i)!=' '||str.charAt(i)!='.'||str.charAt(i)!=',')){
                temp+=str.charAt(i);
                i++;
            }
            if(i<str.length()&&(str.charAt(i)==' '||str.charAt(i)=='.'||str.charAt(i)==',')){
                wordsList.add(Pair.create(temp,i));
                i++;
            }
        }
    }

    public void promptSpeechInput(){
        Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL,
                RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, Locale.getDefault());
        intent.putExtra(RecognizerIntent.EXTRA_PROMPT,"Say something&#8230;");
        try {
            startActivityForResult(intent, REQ_CODE_SPEECH_INPUT);
        } catch (ActivityNotFoundException a) {
            Toast.makeText(getApplicationContext(),
                    "Sorry! Your device doesn\\'t support speech input",
                    Toast.LENGTH_SHORT).show();
        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        switch (requestCode) {
            case REQ_CODE_SPEECH_INPUT: {
                if (resultCode == RESULT_OK && null != data) {

                    ArrayList<String> result = data
                            .getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS);
                    Log.v("ARCHIT",result.get(0)+result.get(1));
                }
                break;
            }

        }
    }
}
