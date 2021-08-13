package com.test;

public class challenge_43 {
    public static int[] coulumnElementsIn(int[][] matrix, int num){
        int[] ret = new int[matrix.length * num];
        int index = 0;
        for (int i=0; i<num; i++){
            for (int j=0; j<matrix.length; j++){
                ret[index] = matrix[j][i];
                index ++;
            }
        }
        return ret;
    }

    public static String[] coulumnElementsIn(String[][] matrix, int num){
        String[] ret = new String[matrix.length * num];
        int index = 0;
        for (int i=0; i<num; i++){
            for (int j=0; j<matrix.length; j++){
                ret[index] = matrix[j][i];
                index ++;
            }
        }
        return ret;
    }
}
