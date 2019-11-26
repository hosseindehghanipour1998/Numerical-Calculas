package com.company.Dehghanipour.Hossein;

public class Guassian {

    public int checkColumn(float[][] matrix , int column){
        int row = -1 ;
        for ( int  i = 0 ; i < matrix[column].length/2 ; i++){
            if ( matrix[column][i] == 0){
                return i ;
            }
        }
        return row ;
    }

    public void swapRow(int theRow , int withTheRow , float[][] matrix){
        for ( int column = 0 ; column < matrix[theRow].length ; column++){
            float temp = matrix[theRow][column] ;
            matrix[theRow][column] = matrix[withTheRow][column];
            matrix[withTheRow][column] = temp ;
        }
    }

    public void start(float[][] matrix){
        int column = 0 ;
        int row = 0 ;
        int martabe = 0 ;
        for(martabe = 0 ; martabe < matrix.length-1 ; martabe++){
            column = 0 ;
            for( row = 0 ; row < matrix[column].length - 1 ; row++ , column++){
                float coefficient = (matrix[row+1][column]/matrix[martabe][column]) * -1 ;
                for(int tempColumn = 0 ; tempColumn < matrix[column].length ; tempColumn++){
                    matrix[row+1][tempColumn] += matrix[row][tempColumn] * coefficient ;
                }
            }
        }

    }

    public void printMatrix(float[][] matrix){
        for(int i = 0 ; i < matrix.length ; i++){
            for(int j = 0 ; j < matrix.length ; j++){
                System.out.print(  matrix[i][j] +" |");
            }
            System.out.println();
        }
    }
}
