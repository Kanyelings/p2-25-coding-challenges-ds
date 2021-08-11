package com.test;

public class challenge_42 {
    public static boolean intersect(double[] c1, double[] c2){
        double x1=c1[0], y1=c1[1], r1=c1[2];
        double x2=c2[0], y2=c2[1], r2=c2[2];
        double main = r1;
        boolean ret = false;
        if (r2 > r1)
            main = r2;
        if ( (Math.abs(r1-r2)) > Math.sqrt(Math.pow((x1-x2), 2) + Math.pow((y1-y2), 2))){
            ret = true;
            if (Math.sqrt(Math.pow((x1-x2), 2) + Math.pow((y1-y2), 2)) < main)
                ret = false;
        }
        return ret;
    }
}
