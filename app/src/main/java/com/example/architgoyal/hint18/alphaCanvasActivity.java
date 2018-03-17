package com.example.architgoyal.hint18;

import android.content.Intent;
import android.graphics.Bitmap;
import android.os.Build;
import android.speech.tts.TextToSpeech;
import android.support.annotation.RequiresApi;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.MotionEvent;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.Locale;

public class alphaCanvasActivity extends AppCompatActivity implements TextToSpeech.OnInitListener {

    public TextView alp_image;
    public int i=0;
    public TextToSpeech tts;
    private MyDrawView myDrawView;

    @RequiresApi(api = Build.VERSION_CODES.JELLY_BEAN_MR1)

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_alpha_canvas);
        getSupportActionBar().setTitle("Draw Alphabets");

        tts = new TextToSpeech(this, this);
        alp_image=(TextView)findViewById(R.id.alphabet_image);
        final LinearLayout draw_area=(LinearLayout)findViewById(R.id.llMain);
        //LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams((int)(width-width%28),(int)(width-width%28));
        //draw_area.setLayoutParams(lp);
        Button redraw=(Button)findViewById(R.id.redraw);
        final Button next=(Button)findViewById(R.id.next);


        CharacterList.list=new ArrayList<String>();
        CharacterList.setList();
        alp_image.setText(CharacterList.list.get(i++));
        speakOut();
        //CharacterList.list.remove(0);

        myDrawView = new MyDrawView(this);
        TimeList.list.clear();
        draw_area.addView(myDrawView);
        //draw_area.setDrawingCacheEnabled(true);

        redraw.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                draw_area.removeAllViews();
                myDrawView=new MyDrawView(alphaCanvasActivity.this);
                TimeList.list.clear();
                draw_area.addView(myDrawView);
                //draw_area.setDrawingCacheEnabled(true);
                //drawn_image=null;
            }
        });
        next.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                TimeList.list.add(String.valueOf(myDrawView.endTime-myDrawView.sstartTime));

                for(int i=0;i<TimeList.list.size();i++){
                    Log.v("GOY","ss"+TimeList.list.get(i)+"xx");
                }

                draw_area.setDrawingCacheEnabled(true);
                Bitmap drawn_image = draw_area.getDrawingCache();
                /*JSONObject jobj=new JSONObject();
                try {
                    jobj.put("letter",alp_image.getText());
                    jobj.put("Image",getStringFromBitmap(drawn_image));
                    jobj.put("id","1");
                } catch (JSONException e) {
                    e.printStackTrace();
                } catch (UnsupportedEncodingException e) {
                    e.printStackTrace();
                }
                Log.e("QWERTY",jobj.toString());
                new SendDeviceDetails().execute(Domain.ip+"req_image/",jobj.toString());*/

                if(i!=CharacterList.list.size()){
                    alp_image.setText("");
                    alp_image.setText(CharacterList.list.get(i++));
                    speakOut();}
                else{
                    startActivity(new Intent(alphaCanvasActivity.this,MainActivity.class));
                }

                draw_area.removeAllViews();
                myDrawView=new MyDrawView(alphaCanvasActivity.this);
                TimeList.list.clear();
                draw_area.addView(myDrawView);
                draw_area.setDrawingCacheEnabled(false);
                //drawn_image=null;
            }
        });
    }

    @Override
    public void onDestroy() {
        // Don't forget to shutdown tts!
        if (tts != null) {
            tts.stop();
            tts.shutdown();
        }
        super.onDestroy();
    }

    @Override
    public void onInit(int status) {

        if (status == TextToSpeech.SUCCESS) {

            int result = tts.setLanguage(Locale.US);

            if (result == TextToSpeech.LANG_MISSING_DATA
                    || result == TextToSpeech.LANG_NOT_SUPPORTED) {
                Log.e("TTS", "This Language is not supported");
            } else {
                speakOut();
            }

        } else {
            Log.e("TTS", "Initilization Failed!");
        }

    }

    private void speakOut() {

        String text = alp_image.getText().toString();

        tts.speak(text, TextToSpeech.QUEUE_FLUSH, null);
    }

    void measureTime(MyDrawView drawView){

    }
}
