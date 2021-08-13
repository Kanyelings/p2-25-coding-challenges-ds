package com.test;

import javax.swing.*;

public class challenge_40 {
    public static int[] bubbleSort(int[] unsorted){
        int after = 0, before=0, count=0;
        while (count != unsorted.length) {
            for (int i = 0; i < unsorted.length - 1 - count; i++) {
                before = unsorted[i];
                after = unsorted[i + 1];
                if (before > after){
                    unsorted[i] = after;
                    unsorted[i + 1] = before;
                }
            }
            count ++;
        }
        return unsorted;
    }
}
