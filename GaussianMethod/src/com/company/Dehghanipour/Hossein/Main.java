package com.company.Dehghanipour.Hossein;

import java.util.Random;

public class Main {

    public static void main(String[] args) {
	// write your code here
        int N = 3 ;
        float[][] matrix = new float[N][N];
        Random r = new Random();
        for(int i = 0 ; i < N ; i++){
            for(int j = 0 ; j < N ; j++){
                float number = r.nextFloat() + 1 ;
                matrix[i][j] = number ;
            }
        }

        Guassian g = new Guassian();
        g.start(matrix);
        g.printMatrix(matrix);
    }
}
