```java
package com.example.mainpad;

import androidx.appcompat.app.AppCompatActivity;

import android.net.DhcpInfo;
import android.net.wifi.WifiManager;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    Button button;
    ArrayList<Socket> socketList;
    ServerSocket serverSocket;
    int index;
    OutputStream outputStream;
    DataOutputStream dataOutputStream;
    Socket tempSocket;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        button = findViewById(R.id.button);
        socketList = new ArrayList<>();
        index = 0;

        WifiManager wm = (WifiManager) getSystemService(WIFI_SERVICE);

        DhcpInfo dhcpInfo = wm.getDhcpInfo() ;

        int serverIp = dhcpInfo.ipAddress;
        String ipAddress = String.format("%d.%d.%d.%d", (serverIp & 0xff),
                (serverIp >> 8 & 0xff),
                (serverIp >> 16 & 0xff),
                (serverIp >> 24 & 0xff));
        System.out.println("----"+ipAddress);
        Log.d("ip ",ipAddress);

        try {
            serverSocket = new ServerSocket(8889);
        } catch (IOException e) {
            e.printStackTrace();
        }

        Runnable runnable = new Runnable() {

            Socket socket;

            @Override
            public void run() {
                Log.d("server","socket is start");
                while(true){
                    try {
                        socket = serverSocket.accept();
                        socketList.add(socket);
                        Log.e("socket","is accepted");
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }
        };
        Thread ServerSocketThread = new Thread(runnable);
        ServerSocketThread.start();
    }

    public void ButtonClick(View v) {
        for(int i=0;i<socketList.size();i++){

            tempSocket = socketList.get(i);
            Runnable sendRun = new Runnable() {
                @Override
                public void run() {
                    try {
                        outputStream = tempSocket.getOutputStream();
                        dataOutputStream = new DataOutputStream(outputStream);
                        dataOutputStream.writeUTF(index+"th send");
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            };
            Thread sendThread = new Thread(sendRun);
            sendThread.start();
        }
        index++;
    }


}

```

