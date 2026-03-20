{-
Module      : 1JC3-Assign1.Assign_1.hs
Copyright   :  (c) Curtis D'Alves 2022
License     :  GPL (see the LICENSE file)
Maintainer  :  none
Stability   :  experimental
Portability :  portable

Description:
  Assignment 1 -- McMaster CS 1JC3 2025.

  Modified by W. M. Farmer 13 September 2025.
-}
module Assign_1 where

-----------------------------------------------------------------------------------------------------------
-- INSTRUCTIONS              README!!!
-----------------------------------------------------------------------------------------------------------
-- 1) DO NOT DELETE/ALTER ANY CODE ABOVE THESE INSTRUCTIONS AND DO NOT ADD ANY IMPORTS
-- 2) DO NOT REMOVE / ALTER TYPE DECLERATIONS (I.E THE LINE WITH THE :: ABOUT THE FUNCTION DECLERATION)
--    IF YOU ARE UNABLE TO COMPLETE A FUNCTION, LEAVE IT'S ORIGINAL IMPLEMENTATION (I.E. THROW AN ERROR)
-- 3) MAKE SURE THE PROJECT COMPILES (I.E. RUN STACK BUILD AND MAKE SURE THERE ARE NO ERRORS) BEFORE
--    SUBMITTING, FAILURE TO DO SO WILL RESULT IN A MARK OF 0
-- 4) REPLACE macid = "TODO" WITH YOUR ACTUAL MACID (EX. IF YOUR MACID IS jim THEN macid = "jim")
-----------------------------------------------------------------------------------------------------------

-- Name: Colin Wei
-- Date: September 23, 2025
macid :: String
macid = "weic39"

(***) :: Double -> Double -> Double
x *** y = if x >= 0 then x ** y else -((-x) ** y)

(===) :: Double -> Double -> Bool
x === y =
  let tol = 1e-3
  in abs (x-y) <= tol

{- -----------------------------------------------------------------
 - cubicQ
 - -----------------------------------------------------------------
 - Description:
 -   Finds the Q value using A, B, and C
 -}
cubicQ :: Rational -> Rational -> Rational -> Rational
cubicQ a b c = (3*a*c-b^2)/(9*(a^2))

{- -----------------------------------------------------------------
 - cubicR
 - -----------------------------------------------------------------
 - Description:
 -   Finds the R value using A, B, C and D
 -}
cubicR :: Rational -> Rational -> Rational -> Rational -> Rational
cubicR a b c d = (9*a*b*c - 27*(a^2)*d - 2*(b^3))/(54*(a^3))

{- -----------------------------------------------------------------
 - cubicDiscSign
 - -----------------------------------------------------------------
 - Description:
 -   Determines the sign of the discriminant using Q and R
 -   Returns -1 if negative, 0 if neutral, and 1 if positive
 -}
cubicDiscSign :: Rational -> Rational -> Int
cubicDiscSign q r
  |  disc > 0 = 1
  |  disc == 0 = 0
  |  otherwise = -1
  where disc = q^^3 + r^^2

{-  let disc = q^^3 + r^^2
  in 
  disc > 0 = 1
  disc == 0 = 0
  otherwise = -1
-}

{- -----------------------------------------------------------------
 - cubicS
 - -----------------------------------------------------------------
 - Description:
 -   Finds the S value using Q and R
 -}
cubicS :: Rational -> Rational -> Double
cubicS q r = (fromRational r + sqrt(fromRational q^3 + fromRational r^2))***(1/3)

{- -----------------------------------------------------------------
 - cubicT
 - -----------------------------------------------------------------
 - Description:
 -   Finds the T value
 -}
cubicT :: Rational -> Rational -> Double
cubicT q r = (fromRational r - sqrt(fromRational q^3 + fromRational r^2))***(1/3)

{- -----------------------------------------------------------------
 - cubicRealSolutions
 - -----------------------------------------------------------------
 - Description:
 -   Finds the solution to the cubic equation using A, B, C and D
 -}
cubicRealSolutions :: Rational -> Rational -> Rational -> Rational -> [Double]
cubicRealSolutions a b c d
  | a == 0      = []
  | sign == -1  = []
  | sign ==  0  = [x1, x2, x2]
  | sign ==  1  = [x1]
  | otherwise   = []
  where
    sign = cubicDiscSign q r
    s    = cubicS q r
    t    = cubicT q r
    q    = cubicQ a b c
    r    = cubicR a b c d
    x1 = s + t - fromRational b / (3 * fromRational a)
    x2 = - ((s + t) / 2) - fromRational b / (3 * fromRational a)

{- -----------------------------------------------------------------
 - Test Cases
 - -----------------------------------------------------------------
 -}

-- TODO: Add Test Cases for each of your functions below here
-- cubicS (-3) 2 -> returns NaN