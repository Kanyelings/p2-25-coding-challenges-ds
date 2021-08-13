package com.test;

public class challenge_41 {
    public static double seperationLength(double[] a, double[] b){
        return Math.pow(Math.pow((a[0]-b[0]), 2) + Math.pow((a[1]-b[1]), 2), 0.5);
    }
}
