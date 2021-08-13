package com.test;

public class challenge_44 {
    public static int toDecimal(int binary){
        int len = Integer.toString(binary).length();
        int ret = 0;
        for (int i=0; i<len; i++){
            System.out.println(binary);
            ret += (binary % 10) * Math.pow(2, i);
            binary = (int) Math.floor(binary / (double) 10);
        }
        return ret;
    }
}
