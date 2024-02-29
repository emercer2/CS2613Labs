#lang racket

(define (finalVel time)
  (define vi 5)
  (define a 0.5)
  ;(define vi 32)
  ;(define a -0.35)

  (+ vi (* a time))
)

(finalVel 1)
