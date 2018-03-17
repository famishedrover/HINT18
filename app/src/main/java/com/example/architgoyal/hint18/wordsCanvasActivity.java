package com.example.architgoyal.hint18;

import android.content.Intent;
import android.graphics.Bitmap;
import android.os.Build;
import android.speech.tts.TextToSpeech;
import android.support.annotation.RequiresApi;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.Locale;
import java.util.Random;

public class wordsCanvasActivity extends AppCompatActivity implements TextToSpeech.OnInitListener {

    public ImageView alp_image;
    //public LinearLayout draw_area;
    public TextView image_name;
    //public Bitmap drawn_image;
    public int i=0;
    public TextToSpeech tts;

    @RequiresApi(api = Build.VERSION_CODES.JELLY_BEAN_MR1)

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_words_canvas);
        getSupportActionBar().setTitle("Draw Words");

        tts = new TextToSpeech(this, this);
        alp_image=(ImageView)findViewById(R.id.alphabet_image);
        final LinearLayout draw_area=(LinearLayout)findViewById(R.id.llMain);
        image_name=(TextView)findViewById(R.id.text);
        //LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams((int)(width-width%28),(int)(width-width%28));
        //draw_area.setLayoutParams(lp);
        ImageList.set();
        Button redraw=(Button)findViewById(R.id.redraw);
        final Button next=(Button)findViewById(R.id.next);
        alp_image.setImageResource(ImageList.textimage.get(i).second.get(new Random().nextInt(3)));
        image_name.setText(ImageList.textimage.get(i).first.toString());
        i++;
        //ImageList.textimage.remove(0);
        speakOut();

        final MyDrawView myDrawView = new MyDrawView(this);
        draw_area.addView(myDrawView);
        //draw_area.setDrawingCacheEnabled(true);

        redraw.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                draw_area.removeAllViews();
                MyDrawView myDrawView1=new MyDrawView(wordsCanvasActivity.this);
                draw_area.addView(myDrawView1);
            }
        });
        next.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                draw_area.setDrawingCacheEnabled(true);
                Bitmap drawn_image = draw_area.getDrawingCache();
                /*JSONObject jobj=new JSONObject();
                try {
                    jobj.put("letter",image_name.getText());
                    jobj.put("Image",getStringFromBitmap(drawn_image));
                    jobj.put("id","1");
                } catch (JSONException e) {
                    e.printStackTrace();
                }
                new SendDeviceDetails().execute(Domain.ip+"req_word/",jobj.toString());*/
                if(ImageList.textimage.size()!=i){
                    alp_image.setImageResource(ImageList.textimage.get(i).second.get(new Random().nextInt(3)));
                    image_name.setText(ImageList.textimage.get(i).first.toString());
                    i++;
                    speakOut();}
                else{
                    startActivity(new Intent(wordsCanvasActivity.this,MainActivity.class));
                }
                draw_area.removeAllViews();
                MyDrawView myDrawView1=new MyDrawView(wordsCanvasActivity.this);
                draw_area.addView(myDrawView1);
                draw_area.setDrawingCacheEnabled(false);
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

        String text = image_name.getText().toString();

        tts.speak(text, TextToSpeech.QUEUE_FLUSH, null);
    }
}
