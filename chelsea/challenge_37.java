package com.test;

public class challenge_37 {
    public static int[] asciiValues(String text){
        int[] ret = new int[text.length()];
        for (int i=0; i<text.length(); i++){
            ret[i] = (int) text.charAt(i);
        }
        return ret;
    }
}
