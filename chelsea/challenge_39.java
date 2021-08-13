package com.test;

public class challenge_39 {
    public static String caeserEncript(String text, int key){
        StringBuilder ret = new StringBuilder();
        for (int i=0; i<text.length(); i++){
            if ((int) text.charAt(i) <= 90)
                if ((int) text.charAt(i) > 90-key)
                    ret.append(Character.toString((((int) text.charAt(i) + key) % 90) + 64));
                else
                    ret.append(Character.toString(((int) text.charAt(i) + key)));
            else
                if ((int) text.charAt(i) > 122-key)
                    ret.append(Character.toString((((int) text.charAt(i) + key) % 122) + 96));
                else
                    ret.append(Character.toString(((int) text.charAt(i) + key)));
        }
        return ret.toString();
    }
}

