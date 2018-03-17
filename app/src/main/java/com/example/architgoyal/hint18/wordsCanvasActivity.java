package com.example.architgoyal.hint18;

import android.content.Intent;
import android.graphics.Bitmap;
import android.os.AsyncTask;
import android.os.Build;
import android.speech.tts.TextToSpeech;
import android.support.annotation.RequiresApi;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Base64;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.ByteArrayOutputStream;
import java.io.DataOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.Locale;
import java.util.Random;

public class wordsCanvasActivity extends AppCompatActivity implements TextToSpeech.OnInitListener {

    public ImageView alp_image;
    //public LinearLayout draw_area;
    public TextView image_name;
    //public Bitmap drawn_image;
    public int i=0;
    public TextToSpeech tts;
    private MyDrawView myDrawView;
    private LinearLayout draw_area;

    @RequiresApi(api = Build.VERSION_CODES.JELLY_BEAN_MR1)

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_words_canvas);
        getSupportActionBar().setTitle("Draw Words");

        tts = new TextToSpeech(this, this);
        alp_image=(ImageView)findViewById(R.id.alphabet_image);
        draw_area=(LinearLayout)findViewById(R.id.llMain);
        image_name=(TextView)findViewById(R.id.text);
        //LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams((int)(width-width%28),(int)(width-width%28));
        //draw_area.setLayoutParams(lp);
        ImageList.apple=new ArrayList<Integer>();
        ImageList.mango=new ArrayList<Integer>();
        ImageList.dog=new ArrayList<Integer>();
        ImageList.cat=new ArrayList<Integer>();
        ImageList.house=new ArrayList<Integer>();
        ImageList.set();
        Button redraw=(Button)findViewById(R.id.redraw);
        final Button next=(Button)findViewById(R.id.next);
        alp_image.setImageResource(ImageList.textimage.get(i).second.get(new Random().nextInt(3)));
        image_name.setText(ImageList.textimage.get(i).first.toString());
        i++;
        //ImageList.textimage.remove(0);
        speakOut();

        myDrawView = new MyDrawView(this);
        TimeList.list.clear();
        draw_area.addView(myDrawView);
        //draw_area.setDrawingCacheEnabled(true);

        redraw.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                draw_area.removeAllViews();
                myDrawView=new MyDrawView(wordsCanvasActivity.this);
                TimeList.list.clear();
                draw_area.addView(myDrawView);
            }
        });
        next.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                TimeList.list.add(String.valueOf(myDrawView.endTime-myDrawView.sstartTime));
                int sum=0;
                for(int i=0;i<TimeList.list.size()-1;i++){
                    sum+=Integer.parseInt(TimeList.list.get(i));
                    Log.v("GOY","ss"+TimeList.list.get(i)+"xx");
                }
                draw_area.setDrawingCacheEnabled(true);
                Bitmap drawn_image = draw_area.getDrawingCache();
                JSONObject jobj=new JSONObject();
                try {
                    jobj.put("child_id","1");
                    jobj.put("word",image_name.getText());
                    jobj.put("score","0");
                    jobj.put("total_time",TimeList.list.get(TimeList.list.size()-1));
                    jobj.put("no_of_strokes",TimeList.list.size()-1);
                    jobj.put("total_length","0");
                    jobj.put("time_delay",String.valueOf(Integer.parseInt(TimeList.list.get(TimeList.list.size()-1))-sum));
                    jobj.put("Image",getStringFromBitmap(drawn_image));
                } catch (JSONException e) {
                    e.printStackTrace();
                }
                Log.e("QWERTY",jobj.toString());
                new SendDeviceDetails().execute(Domain.ip+"/webhook/wresponse",jobj.toString());
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

    public String getStringFromBitmap(Bitmap image){
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        image.compress(Bitmap.CompressFormat.JPEG, 100, baos); //bm is the bitmap object
        byte[] b = baos.toByteArray();
        return Base64.encodeToString(b, Base64.DEFAULT);
    }

    private class SendDeviceDetails extends AsyncTask<String, Void, String> {

        @Override
        protected String doInBackground(String... params) {

            String data = "";

            HttpURLConnection httpURLConnection = null;
            try {

                httpURLConnection = (HttpURLConnection) new URL(params[0]).openConnection();
                httpURLConnection.setRequestMethod("POST");

                httpURLConnection.setDoOutput(true);

                DataOutputStream wr = new DataOutputStream(httpURLConnection.getOutputStream());
                wr.writeBytes(params[1]);
                wr.flush();
                wr.close();

                InputStream in = httpURLConnection.getInputStream();
                InputStreamReader inputStreamReader = new InputStreamReader(in);

                int inputStreamData = inputStreamReader.read();
                while (inputStreamData != -1) {
                    char current = (char) inputStreamData;
                    inputStreamData = inputStreamReader.read();
                    data += current;
                }
            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                if (httpURLConnection != null) {
                    httpURLConnection.disconnect();
                }
            }

            return data;
        }

        @Override
        protected void onPostExecute(String result) {
            super.onPostExecute(result);
            Log.e("ARCHIT", result);
            if(ImageList.textimage.size()!=i){
                alp_image.setImageResource(ImageList.textimage.get(i).second.get(new Random().nextInt(3)));
                image_name.setText(ImageList.textimage.get(i).first.toString());
                i++;
                speakOut();}
            else{
                startActivity(new Intent(wordsCanvasActivity.this,MainActivity.class));
            }
            draw_area.removeAllViews();
            myDrawView=new MyDrawView(wordsCanvasActivity.this);
            TimeList.list.clear();
            draw_area.addView(myDrawView);
            draw_area.setDrawingCacheEnabled(false);
        }
    }
}
