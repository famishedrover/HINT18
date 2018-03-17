package com.example.architgoyal.hint18;

/**
 * Created by architgoyal on 17/03/18.
 */
import android.content.Context;
import android.content.Intent;
import android.os.AsyncTask;
import android.support.v4.view.PagerAdapter;
import android.support.v7.widget.CardView;
import android.util.Log;
import android.util.Pair;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.DataOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

public class CardPagerAdapter extends PagerAdapter implements CardAdapter {

    private List<CardView> mViews;
    private List<CardItem> mData;
    private float mBaseElevation;
    private Context context;
    private String Url=Domain.ip+"/webhook/letter";

    public CardPagerAdapter() {
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
        context=container.getContext();
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
                JSONObject jobj=new JSONObject();
                if(position==0){
                    CharacterList.list=null;
                    try {
                        jobj.put("id","1");
                        jobj.put("number","5");
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                }
                else if(position==1){
                    CharacterList.list=null;
                    try {
                        jobj.put("id","1");
                        jobj.put("number","10");
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                }
                else if(position==2){
                    CharacterList.list=null;
                    try {
                        jobj.put("id","1");
                        jobj.put("number","15");
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                }
                else if(position==3){
                    CharacterList.list=null;
                    try {
                        jobj.put("id","1");
                        jobj.put("number","20");
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                }
                new SendDeviceDetails().execute(Url,jobj.toString());
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
            try {
                JSONObject jobj=new JSONObject(result);
                JSONArray arr=jobj.getJSONArray("symbols");
                CharacterList.list=new ArrayList<Pair<String,String>>();
                for(int i=0;i<arr.length();i++){
                    JSONArray two=arr.getJSONArray(i);
                    CharacterList.list.add(Pair.create(two.get(0).toString(),two.get(1).toString()));
                }
            } catch (JSONException e) {
                e.printStackTrace();
            }
            context.startActivity(new Intent(context,alphaCanvasActivity.class));
        }
    }
}