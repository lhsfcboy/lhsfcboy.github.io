#lang planet neil/sicp
(define (sumBigger a b c)  
    (define (min a b)  
    (if (> a b)  
        (b)  
        a))  
    (- (+ a b c) (min (min a b) c)))

(sumBigger 1 2 3)  