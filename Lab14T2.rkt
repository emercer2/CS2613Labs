#lang racket

(define (oneToSixity)
  (range 0 60)
)

(define (matching lst1 lst2 strtPos)
  (define tol 1)
  (cond
    [(equal? strtPos (- (length lst1) 1)) -1]
    [else
     (cond
       [(and (<= (list-ref lst2 strtPos) (+ (list-ref lst1 strtPos) tol)) (>= (list-ref lst2 strtPos) (list-ref lst1 strtPos) tol))
        (matching lst1 lst2 (+ 1 strtPos))
       ]
       [else strtPos]
     )
    ]
  )
)

(matching '(1 2 3 4 5 6 8 8) '(1 2 3 4 5 6 9 8) 0)