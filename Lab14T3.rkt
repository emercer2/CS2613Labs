#lang racket

(define (same-speed func1 func2 times)
  (define finVel1 (map func1 times))
  (define finVel2 (map func2 times))
  (matching finVel1 finVel2 0)
)

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
        strtPos
       ]
       [else (matching lst1 lst2 (+ 1 strtPos))]
     )
    ]
  )
)


(define (accel time)
  (define vi 5)
  (define a 0.5)

  (+ vi (* a time))
)


(define (decel time)
  (define vi 32)
  (define a -0.35)

  (+ vi (* a time))
)

(same-speed accel decel (oneToSixity))