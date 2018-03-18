package com.example.architgoyal.hint18;

import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.graphics.Color;
import android.icu.text.RelativeDateTimeFormatter;
import android.speech.RecognizerIntent;
import android.support.v4.util.Pair;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.Spannable;
import android.text.SpannableString;
import android.text.style.AbsoluteSizeSpan;
import android.text.style.ForegroundColorSpan;
import android.text.style.RelativeSizeSpan;
import android.util.Log;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Locale;

public class readActivity extends AppCompatActivity {

    private TextView tv,tv3;
    private Spannable spannable;
    private String str;
    private HashMap<String,Pair<Integer,Integer>> wordsList;
    private ArrayList<String> speechList;
    private HashMap<String,Boolean> spoken=new HashMap<String,Boolean>();
    private String temp="";
    private final int REQ_CODE_SPEECH_INPUT = 100;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_read);
        getSupportActionBar().setTitle("Read & Speak");

        tv=(TextView)findViewById(R.id.text_view);
        tv3=(TextView)findViewById(R.id.tv3);
        str=tv.getText().toString();
        spannable = new SpannableString(str);
        createWordsList();
        promptSpeechInput();
    }

    public void createWordsList(){
        wordsList=new HashMap<String,Pair<Integer,Integer>>();

        int i=0,x=0;
        while(i<str.length()){
            String temp="";
            while(i<str.length()&&str.charAt(i)!=' '&&str.charAt(i)!='.'&&str.charAt(i)!=','){
                temp+=str.charAt(i);
                i++;
            }
            if(i<str.length()&&(str.charAt(i)==' '||str.charAt(i)=='.'||str.charAt(i)==',')){
                wordsList.put(temp,Pair.create(i,x));
                x=i;
                i++;
            }
        }
        Log.v("words",str.length()+wordsList.keySet().toString());
    }

    private void promptSpeechInput() {
        Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL,
                RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, Locale.getDefault());
        intent.putExtra(RecognizerIntent.EXTRA_PROMPT,
                "Say something");
        try {
            startActivityForResult(intent, REQ_CODE_SPEECH_INPUT);
        } catch (ActivityNotFoundException a) {
            Toast.makeText(getApplicationContext(),
                    "Sorry! Your device doesn\'t support speech input",
                    Toast.LENGTH_SHORT).show();
        }
    }

    /**
     * Receiving speech input
     * */
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        switch (requestCode) {
            case REQ_CODE_SPEECH_INPUT: {
                if (resultCode == RESULT_OK && null != data) {

                    ArrayList<String> result = data
                            .getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS);
                    Log.v("ARCH",result.get(0));
                    createWordsListSpeech(result.get(0));
                    matchWords();
                }
                break;
            }

        }
    }

    public void createWordsListSpeech(String strg){
        speechList=new ArrayList<String>();

        int i=0;
        while(i<strg.length()){
            String temp="";
            while(i<strg.length()&&strg.charAt(i)!=' '&&strg.charAt(i)!='.'&&strg.charAt(i)!=','){
                temp+=strg.charAt(i);
                i++;
            }
            if(i<strg.length()&&(strg.charAt(i)==' '||strg.charAt(i)=='.'||strg.charAt(i)==',')){
                speechList.add(temp);
                i++;
            }
        }

        for (int j=0;j<speechList.size();j++){
            Log.v("speech",speechList.get(j));
        }
    }

    public void matchWords(){
        tv.setTextColor(Color.RED);
        for(int i=0;i<speechList.size();i++){
            Log.v("one",speechList.get(i));
            if(wordsList.containsKey(speechList.get(i))){
                spoken.put(speechList.get(i),true);
                spannable.setSpan(new ForegroundColorSpan(Color.GREEN), wordsList.get(speechList.get(i)).second,wordsList.get(speechList.get(i)).first, Spannable.SPAN_EXCLUSIVE_EXCLUSIVE);
                spannable.setSpan(new RelativeSizeSpan(0.5f),wordsList.get(speechList.get(i)).second,wordsList.get(speechList.get(i)).first, Spannable.SPAN_EXCLUSIVE_EXCLUSIVE);
            }
        }
        tv.setText(spannable);
        populateList();
    }

    public void populateList(){
        for ( String key : wordsList.keySet() ) {
            if(!spoken.containsKey(key)){
                temp+=key+"\n";
            }
        }
        tv3.setText(temp);
    }
}
