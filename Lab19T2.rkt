#lang racket
(require racket/class)

(define point% (class object%
                   (super-new)
                 (define/public (distance other) (sqrt (+ (+ (expt (- x (send other get-x)) 2) (expt (- y (send other get-y)) 2) (expt (- z (send other get-z)) 2)))))
                 (define/public (distance-range other range) (if (>= (distance other) range) false true))
                 (define/public (triangle-perimiter p1 p2) (+ (distance p1) (+ (send p1 distance p2) (distance p2))))
                 (define/public (set-x nx) (set! x nx))
                 (define/public (set-y ny) (set! y ny))
                 (define/public (set-z nz) (set! z nz))
                 (define/public (get-x) x)
                 (define/public (get-y) y)
                 (define/public (get-z) z)
                   (init-field x y z)))

(define p1 (make-object point% 9 3 6))
(define p2 (make-object point% -1 2 8))
(define p3 (make-object point% -1 3 4))
(send p1 distance p2)
(send p1 distance-range p2 10) 
(send p1 triangle-perimiter p2 p3) 
