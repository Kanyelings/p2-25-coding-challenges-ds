package com.test;

public class challenge_36 {
    public static Character[] stringArray(String text) {
        Character[] ret = new Character[text.length()];
        for (int i=0; i<text.length(); i++){
            ret[i] = text.charAt(i);
        }
        return ret;
    }
}
