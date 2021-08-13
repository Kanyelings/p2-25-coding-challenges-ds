package com.test;

public class challenge_38 {
    public static String stringValue(int[] arr){
        String ret = "";
        for (int i=0; i<arr.length; i++){
            ret += Character.toString(arr[i]);
        }
        return ret;
    }
}
